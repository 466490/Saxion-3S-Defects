
from svgpathtools.parser import parse_path

import svgpathtools.svg_to_paths as reader

import svgpathtools.paths2svg as writer

from svgpathtools.path import Path, Line, is_path_segment

from xml.dom.minidom import parse

from os import path as os_path, makedirs

import re

from tempfile import gettempdir
from xml.dom.minidom import parse as md_xml_parse
from svgwrite import Drawing, text as txt

from math import ceil

from warnings import warn

def write_test(paths=None, colors=None, filename=None, stroke_widths=None,
          nodes=None, node_colors=None, node_radii=None, timestamp=None, 
          margin_size=0.1, mindim=600, dimensions=None, viewbox=None, text=None,
          text_path=None, font_size=None, attributes=None,
          svg_attributes=None, svgwrite_debug=False,
          paths2Drawing=False, mask=None, mask_attributes=None):

    _default_relative_node_radius = 5e-3
    _default_relative_stroke_width = 1e-3
    _default_path_color = '#000000'  # black
    _default_node_color = '#ff0000'  # red
    _default_font_size = 12

    if filename is None:
        timestamp = True if timestamp is None else timestamp
        filename = 'disvg_output.svg'


    # check paths and colors are set
    if isinstance(paths, Path) or is_path_segment(paths):
        paths = [paths]

    if paths:
        if not colors:
            colors = [_default_path_color] * len(paths)
        else:
            print(len(colors), len(paths))
            assert len(colors) == len(paths)
            if isinstance(colors, str):
                colors = writer.str2colorlist(colors,
                                       default_color=_default_path_color)
            elif isinstance(colors, list):
                for idx, c in enumerate(colors):
                    if writer.is3tuple(c):
                        colors[idx] = "rgb" + str(c)

    # check nodes and nodes_colors are set (node_radii are set later)
    if nodes:
        if not node_colors:
            node_colors = [_default_node_color] * len(nodes)
        else:
            assert len(node_colors) == len(nodes)
            if isinstance(node_colors, str):
                node_colors = writer.str2colorlist(node_colors,
                                            default_color=_default_node_color)
            elif isinstance(node_colors, list):
                for idx, c in enumerate(node_colors):
                    if writer.is3tuple(c):
                        node_colors[idx] = "rgb" + str(c)

    # set up the viewBox and display dimensions of the output SVG
    # along the way, set stroke_widths and node_radii if not provided
    assert paths or nodes
    stuff2bound = []
    if viewbox:
        if not isinstance(viewbox, str):
            viewbox = '%s %s %s %s' % viewbox
        if dimensions is None:
            dimensions = viewbox.split(' ')[2:4]
    elif dimensions:
        dimensions = tuple(map(str, dimensions))
        def strip_units(s):
            return re.search(r'\d*\.?\d*', s.strip()).group()
        viewbox = '0 0 %s %s' % tuple(map(strip_units, dimensions))
    else:
        if paths:
            stuff2bound += paths
        if nodes:
            stuff2bound += nodes
        if text_path:
            stuff2bound += text_path
        xmin, xmax, ymin, ymax = writer.big_bounding_box(stuff2bound)
        dx = xmax - xmin
        dy = ymax - ymin

        if dx == 0:
            dx = 1
        if dy == 0:
            dy = 1

        # determine stroke_widths to use (if not provided) and max_stroke_width
        if paths:
            if not stroke_widths:
                sw = max(dx, dy) * _default_relative_stroke_width
                stroke_widths = [sw]*len(paths)
                max_stroke_width = sw
            else:
                assert len(paths) == len(stroke_widths)
                max_stroke_width = max(stroke_widths)
        else:
            max_stroke_width = 0

        # determine node_radii to use (if not provided) and max_node_diameter
        if nodes:
            if not node_radii:
                r = max(dx, dy) * _default_relative_node_radius
                node_radii = [r]*len(nodes)
                max_node_diameter = 2*r
            else:
                assert len(nodes) == len(node_radii)
                max_node_diameter = 2*max(node_radii)
        else:
            max_node_diameter = 0

        extra_space_for_style = max(max_stroke_width, max_node_diameter)
        xmin -= margin_size*dx + extra_space_for_style/2
        ymin -= margin_size*dy + extra_space_for_style/2
        dx += 2*margin_size*dx + extra_space_for_style
        dy += 2*margin_size*dy + extra_space_for_style
        viewbox = "%s %s %s %s" % (xmin, ymin, dx, dy)

        if dx > dy:
            szx = str(mindim) + 'px'
            szy = str(int(ceil(mindim * dy / dx))) + 'px'
        else:
            szx = str(int(ceil(mindim * dx / dy))) + 'px'
            szy = str(mindim) + 'px'
        dimensions = szx, szy

    # Create an SVG file
    if svg_attributes is not None:
        dimensions = (svg_attributes.get("width", dimensions[0]),
                      svg_attributes.get("height", dimensions[1]))
        debug = svg_attributes.get("debug", svgwrite_debug)
        dwg = Drawing(filename=filename, size=dimensions, debug=debug,
                      **svg_attributes)
    else:
        dwg = Drawing(filename=filename, size=dimensions, debug=svgwrite_debug,
                      viewBox=viewbox)

    # add paths
    if paths:
        for i, p in enumerate(paths):
            if isinstance(p, Path):
                ps = p.d()
            elif is_path_segment(p):
                ps = Path(p).d()
            else:  # assume this path, p, was input as a Path d-string
                ps = p

            if attributes:
                good_attribs = {'d': ps}
                for key in attributes[i]:
                    val = attributes[i][key]
                    if key != 'd':
                        try:
                            dwg.path(ps, **{key: val})
                            good_attribs.update({key: val})
                        except Exception as e:
                            warn(str(e))

                dwg.add(dwg.path(**good_attribs))
            else:
                dwg.add(dwg.path(ps, stroke=colors[i],
                                 stroke_width=str(stroke_widths[i]),
                                 fill='none'))

    # add nodes (filled in circles)
    if nodes:
        for i_pt, pt in enumerate([(z.real, z.imag) for z in nodes]):
            dwg.add(dwg.circle(pt, node_radii[i_pt], fill=node_colors[i_pt]))

    # add texts
    if text:
        assert isinstance(text, str) or (isinstance(text, list) and
                                         isinstance(text_path, list) and
                                         len(text_path) == len(text))
        if isinstance(text, str):
            text = [text]
            if not font_size:
                font_size = [_default_font_size]
            if not text_path:
                pos = complex(xmin + margin_size*dx, ymin + margin_size*dy)
                text_path = [Line(pos, pos + 1).d()]
        else:
            if font_size:
                if isinstance(font_size, list):
                    assert len(font_size) == len(text)
                else:
                    font_size = [font_size] * len(text)
            else:
                font_size = [_default_font_size] * len(text)
        for idx, s in enumerate(text):
            p = text_path[idx]
            if isinstance(p, Path):
                ps = p.d()
            elif is_path_segment(p):
                ps = Path(p).d()
            else:  # assume this path, p, was input as a Path d-string
                ps = p

            # paragraph = dwg.add(dwg.g(font_size=font_size[idx]))
            # paragraph.add(dwg.textPath(ps, s))
            pathid = 'tp' + str(idx)
            dwg.defs.add(dwg.path(d=ps, id=pathid))
            txter = dwg.add(dwg.text('', font_size=font_size[idx]))
            txter.add(txt.TextPath('#'+pathid, s))
#TODO: here
    if mask is not None:
        # for each mask
        # create mask...
        
        # clip_path = dwg.defs.add(dwg.mask(defect_type.name)) # name the clip path

        clip_path = dwg.defs.add(dwg.mask(id='newMask')) # name the clip path

        # add rectangle around the mask area... otherwise the method wont work
        # for i, p in enumerate(defect_type.area):
        for i, p in enumerate(mask['mask_area']):
            if isinstance(p, Path):
                ps = p.d()
            elif is_path_segment(p):
                ps = Path(p).d()
            else:  # assume this path, p, was input as a Path d-string
                ps = p

            clip_path.add(dwg.path(ps, stroke='none',
                                 stroke_width=0,
                                 fill='white'))

        # for i, p in enumerate(defect_type.paths):
        for i, p in enumerate(mask['paths']):
            if isinstance(p, Path):
                ps = p.d()
            elif is_path_segment(p):
                ps = Path(p).d()
            else:  # assume this path, p, was input as a Path d-string
                ps = p

            if mask_attributes:
                good_attribs = {'d': ps}
                for key in mask_attributes[i]:
                    val = mask_attributes[i][key]
                    if key != 'd':
                        try:
                            dwg.path(ps, **{key: val})
                            good_attribs.update({key: val})
                        except Exception as e:
                            warn(str(e))

                clip_path.add(dwg.path(**good_attribs))
                
            else:
                clip_path.add(dwg.path(ps, stroke='none',
                                 stroke_width=0,
                                 fill=mask['opacity']))
        # dwg.defs.add(clip_path)

    if paths2Drawing:
        return dwg
      
    # save svg
    # if not os_path.exists(os_path.dirname(filename)):
    #     makedirs(os_path.dirname(filename))
    dwg.save()

    # re-open the svg, make the xml pretty, and save it again
    xmlstring = md_xml_parse(filename).toprettyxml()
    with open(filename, 'w') as f:
        f.write(xmlstring)