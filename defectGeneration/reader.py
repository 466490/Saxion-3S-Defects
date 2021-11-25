from svgpathtools.parser import parse_path

import svgpathtools.svg_to_paths as reader

import svgpathtools.paths2svg as writer

import svgpathtools.path as Path

from xml.dom.minidom import parse

from os import path as os_path, getcwd

def __read(svg_file_location,
              return_svg_attributes=False,
              convert_circles_to_paths=True,
              convert_ellipses_to_paths=True,
              convert_lines_to_paths=True,
              convert_polylines_to_paths=True,
              convert_polygons_to_paths=True,
              convert_rectangles_to_paths=True):

    if os_path.dirname(svg_file_location) == '':
        svg_file_location = os_path.join(getcwd(), svg_file_location)

    old_doc = parse(svg_file_location) # just reads xml
    path_list = {}
    attribute_dictionary_list = {}
    filter_list = {}

    def dom2dict(element):
        """Converts DOM elements to dictionaries of attributes."""
        keys = list(element.attributes.keys())
        values = [val.value for val in list(element.attributes.values())]
        return dict(list(zip(keys, values)))

    for doc in old_doc.getElementsByTagName('g'): # reads all layers
            
        try:
            layer_name = doc.attributes['inkscape:label'].value
        except:
            layer_name = 'unknown'

        # for doc in layer: # reads path from specific layer

        # Use minidom to extract path strings from input SVG
        paths = [dom2dict(el) for el in doc.getElementsByTagName('path')]
        d_strings = [el['d'] for el in paths]
        attribute_dictionary_list[layer_name] = paths

        # Use minidom to extract polyline strings from input SVG, convert to
        # path strings, add to list
        if convert_polylines_to_paths:
            plins = [dom2dict(el) for el in doc.getElementsByTagName('polyline')]
            d_strings += [reader.polyline2pathd(pl) for pl in plins]
            attribute_dictionary_list[layer_name].extend(plins)

        # Use minidom to extract polygon strings from input SVG, convert to
        # path strings, add to list
        if convert_polygons_to_paths:
            pgons = [dom2dict(el) for el in doc.getElementsByTagName('polygon')]
            d_strings += [reader.polygon2pathd(pg) for pg in pgons]
            attribute_dictionary_list[layer_name].extend(pgons)

        if convert_lines_to_paths:
            lines = [dom2dict(el) for el in doc.getElementsByTagName('line')]
            d_strings += [('M' + l['x1'] + ' ' + l['y1'] +
                        'L' + l['x2'] + ' ' + l['y2']) for l in lines]
            attribute_dictionary_list[layer_name].extend(lines)

        if convert_ellipses_to_paths:
            ellipses = [dom2dict(el) for el in doc.getElementsByTagName('ellipse')]
            d_strings += [reader.ellipse2pathd(e) for e in ellipses]
            attribute_dictionary_list[layer_name].extend(ellipses)

        if convert_circles_to_paths:
            circles = [dom2dict(el) for el in doc.getElementsByTagName('circle')]
            d_strings += [reader.ellipse2pathd(c) for c in circles]
            attribute_dictionary_list[layer_name].extend(circles)

        if convert_rectangles_to_paths:
            rectangles = [dom2dict(el) for el in doc.getElementsByTagName('rect')]
            d_strings += [reader.rect2pathd(r) for r in rectangles]
            attribute_dictionary_list[layer_name].extend(rectangles)

        if return_svg_attributes:
            svg_attributes = dom2dict(doc.getElementsByTagName('svg')[0])
            doc.unlink()
            path_list[layer_name] = [parse_path(d) for d in d_strings]
        
        else:
            doc.unlink()
            path_list[layer_name] = [parse_path(d) for d in d_strings]
    
    if return_svg_attributes:
        return path_list, attribute_dictionary_list, svg_attributes
    else:
        return path_list, attribute_dictionary_list 