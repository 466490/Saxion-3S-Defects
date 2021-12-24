import math
import random
import numpy as np
import svgpathtools as svgpt
import wand.image
from xml.dom.minidom import parse, parseString
import reader

class Defect():
    classname = "large_particle"
    parameters = {"layer":{"display_name":"Layer","type":"layer"},
                  "density_mean":{"display_name":"Density mean","type":"float","min":0,"max":10e6,"default":3.0},
                  "density_stddev":{"display_name":"Density stddev","type":"float","min":0,"max":10e6,"default":1.0},
                  "size_mean":{"display_name":"Size mean","type":"float","min":0,"max":10e6,"default":40.0},
                  "size_stddev":{"display_name":"Size stddev","type":"float","min":0,"max":10e6,"default":8.0},
                  "vertices":{"display_name":"Vertices","type":"int","min":0,"max":10e6,"default":18},
                  "angle_variance":{"display_name":"Angle variance","type":"percentage", "default":30},
                  "curviness":{"display_name":"Curviness","type":"percentage", "default":30},
                  "blur":{"display_name":"Blur","type":"percentage", "default":30},
                  "color":{"display_name":"Color","type":"color", "default":"#000000"}}
    

    def __init__(self, srcImg, 
                 density_mean, density_stddev,
                 size_mean, size_stddev,
                 vertices, angle_variance,
                 curviness, blur, color,
                 layer="none"):
        self.srcImg = srcImg
        self.layer = layer
        self.blur = blur/20
        self.area = reader.get_area_of_layer(srcImg, layer)
        self.color = color
        

        self.defects_points = []
        self.defects_bezier_segments = []

        amount_of_defects = self._calculate_amount_of_defects(density_mean, density_stddev, self.area[2], self.area[3])
        for d in range(amount_of_defects):
            self._generate_defect(vertices, angle_variance, self.area, size_mean, size_stddev, curviness)
    
    @classmethod
    def get_classname(cls):
        return cls.classname
    
    @classmethod
    def get_parameters(cls):
        return cls.parameters

    def _generate_defect(self, vertices, angle_variance, area, size_mean, size_stddev, curviness):
        # Calculate all the angles of the defect, this determines the amount of vertices
        angles = self._calculate_angles(vertices, angle_variance)

        # Choose middle point of defect uniformly on area
        middle_point = self._calculate_middle_point(area)

        defect_points = []
        # Add first defect point to array
        defect_points.append(self._calculate_first_point(size_mean, size_stddev, middle_point))

        # Calculate the rest of the defect points based on the previous one
        for index in range(vertices-1):
            new_point = self._calculate_next_point(size_mean, size_stddev, angles[index], defect_points[index], middle_point)
            defect_points.append(new_point)
    
        # Generate the posititon of the control points necessary for the CubicBezier curves
        control_points = self._generate_control_points_pairs(defect_points, curviness)
        
        bezier_segments = []
        # Create the CubicBezier curves based on the points and the control points
        for index in range(len(defect_points)):
            # Prevent list overflow error
            next = 0 if index == len(defect_points)-1 else index+1
            bezier_segments.append(svgpt.CubicBezier(defect_points[index], control_points[index][1],control_points[next][0], defect_points[next]))
        self.defects_points.append(defect_points)
        self.defects_bezier_segments.append(bezier_segments)

    def _calculate_angles(self, vertices, angle_variance):
        total_angle = 0
        angles = []
        for vertice in range(vertices):
            new_angle = abs(np.random.normal(360/vertices, (360/vertices)*(angle_variance/100)))
            total_angle += new_angle
            angles.append(float(new_angle))
        return [360/total_angle*angle for angle in angles]

    def _calculate_amount_of_defects(self, density_mean, density_stddev, width, height):
        # Density is calculated per 1000x1000 pixels
        density_factor = (width*height)/1000000
        density_normal = np.random.normal(density_mean, density_stddev)
        return round((0 if density_normal < 0 else density_normal) * density_factor)
    
    def _calculate_middle_point(self, area):
        return complex(random.uniform(area[0], area[2]+area[0]), random.uniform(area[1], area[3]+area[1]))

    def _calculate_first_point(self, size_mean, size_stddev, offset):
        size = np.random.normal(size_mean, size_stddev)
        random_angle = np.exp(1j*random.uniform(0, 2*math.pi))
        return (0 if size < 0 else size) * random_angle + offset

    def _calculate_next_point(self, distance_mean, distance_stddev, angle, previous_point, middle):
        previous_angle = np.angle(previous_point-middle)
        return np.random.normal(distance_mean, distance_stddev) * np.exp(1j*(np.radians(angle)+previous_angle)) + middle
    
    def _generate_control_points_pairs(self, points, curviness):
        # Generate two control points for each vertice, the control points should be placed optimally  
        # Big brain math time, have fun trying to understand
        control_points_pairs = []
        for index in range(len(points)):
            # Prevent list overflow error
            next = 0 if index == len(points)-1 else index+1
            angle_previous_point = np.arctan2(points[index-1].imag-points[index].imag, points[index-1].real-points[index].real)
            angle_next_point = np.arctan2(points[next].imag-points[index].imag, points[next].real-points[index].real)
            average_angle = (angle_previous_point+angle_next_point)/2

            if angle_previous_point > angle_next_point:
                control1_angle = average_angle + np.radians(90)
                control2_angle = average_angle - np.radians(90)
            else:
                control1_angle = average_angle - np.radians(90)
                control2_angle = average_angle + np.radians(90)
            cp1_distance = np.abs(points[index-1]-points[index])*(curviness/200)+0.00001
            cp2_distance = np.abs(points[index]-points[next])*(curviness/200)+0.00001

            control_point1 = np.exp(1j*control1_angle) * cp1_distance + points[index]
            control_point2 = np.exp(1j*control2_angle) * cp2_distance + points[index]
            control_points_pairs.append((control_point1, control_point2))
        return control_points_pairs
    
    def get_boundingbox(self, index):
        # Get the bbox coords of the defect
        x_min, y_min, x_max, y_max = self._get_boundingbox_coords(index)
        # Create all the bbox lines
        line_top = svgpt.Line(x_min+1j*y_min, x_max+1j*y_min)
        line_right = svgpt.Line(x_max+1j*y_min, x_max+1j*y_max)
        line_bottom = svgpt.Line(x_max+1j*y_max, x_min+1j*y_max)
        line_left = svgpt.Line(x_min+1j*y_max, x_min+1j*y_min)
        # Create path element from the bbox lines
        return svgpt.Path(line_top, line_right, line_bottom, line_left)

    def _get_boundingbox_coords(self, index, offset_multiply=0.2, adjusted=False):
        # Get the defect to calculate bbox for
        defect_points = self.defects_points[index]
        x_max, y_max = -10e6, -10e6
        x_min, y_min = 10e6, 10e6
        # Get the min and max of x and y for each defect
        for point in defect_points:
            if point.real > x_max:
                x_max = point.real
            if point.real < x_min:
                x_min = point.real
            if point.imag > y_max:
                y_max = point.imag
            if point.imag < y_min:
                y_min = point.imag
        if adjusted:
            x_min += abs(self.area[0])
            x_max += abs(self.area[0])
            y_min += abs(self.area[1])
            y_max += abs(self.area[1])
        # Offsets so the bbox is bigger than the defect
        width_offset = (x_max - x_min) * offset_multiply
        height_offset = (y_max - y_min) * offset_multiply
        # Return the bbox coords with the offsets
        return (x_min-width_offset, y_min-height_offset, x_max+width_offset, y_max+height_offset)

    def get_all_bbox_coords(self, offset_multiply=0.2):
        bbox = []
        for defect in range(len(self.defects_points)):
            bbox.append(self._get_boundingbox_coords(defect, offset_multiply, True))
        return bbox

    def get_image_dimensions(self):
        return (self.area[2], self.area[3])

    def preview_image_svg(self, bbox):
        return self._get_image_as_binary("Fast", bbox)

    def preview_image_png(self, bbox):
        with wand.image.Image(blob=self._get_image_as_binary("Accurate", bbox)) as img:
            print("Before")
            return img.make_blob("png")


    def _get_image_as_binary(self, mode, bbox):
        xmlDoc = parse(self.srcImg)
        bboxes = []
        if mode == "Accurate":
            xmlDoc.firstChild.appendChild(self._create_xml_filter(xmlDoc))

        for index in range(len(self.defects_bezier_segments)-1):
            # Create the XML element as a <path> tag
            defect_xml_element = xmlDoc.createElement("path")
            defect_xml_element.setAttribute("filter", "url(#blur_filter)")
            defect_xml_element.setAttribute("d", svgpt.Path(*self.defects_bezier_segments[index]).d())
            defect_xml_element.setAttribute("style", "fill:"+self.color+";fill-opacity:1;stroke:"+self.color+";")

            if bbox:
                bbox_xml_element = xmlDoc.createElement("path")
                bbox_xml_element.setAttribute("d", self.get_boundingbox(index).d())
                bbox_xml_element.setAttribute("style", "fill:none;fill-opacity:1;stroke:red;stroke-width:2;")
                bboxes.append(bbox_xml_element)

            if self.layer != "none":
                # Find correct elements based on layer
                for element in xmlDoc.getElementsByTagName("g"):
                    if element.getAttribute("inkscape:label") == self.layer:
                        element.appendChild(defect_xml_element)
            else:
                # Put defect on top of everything
                xmlDoc.firstChild.appendChild(defect_xml_element)
        # Add bounding boxes add the end to the image last
        for bbox in bboxes:
            xmlDoc.firstChild.appendChild(bbox)
        return xmlDoc.toxml(encoding="UTF-8")

    def _create_xml_filter(self, xmlDoc):
        # Create the filter element as a <filter>
        filter_xml_element = xmlDoc.createElement("filter")
        filter_xml_element.setAttribute("id", "blur_filter")

        feTurbulence_element = parseString('<feTurbulence type="fractalNoise" result="myTurbulence" baseFrequency="0.02" numOctaves="5" seed="2" />')
        filter_xml_element.appendChild(feTurbulence_element.documentElement)
        feComposite_element = parseString('<feComposite operator="in" in="myTurbulence" in2="SourceAlpha" result="myComposite"/>')
        filter_xml_element.appendChild(feComposite_element.documentElement)
        feColorMatrix_element = parseString('<feColorMatrix in="myComposite" result="myColorMatrix" values="0.012 0 0 0 0  0 0.012 0 0 0  0 0 0.012 0 0  2 2 2 0.9 0"></feColorMatrix>')
        filter_xml_element.appendChild(feColorMatrix_element.documentElement)

        # Create the Gaussian blur element as a <feGaussianBlur> tag
        blur_xml_element = xmlDoc.createElement("feGaussianBlur")
        blur_xml_element.setAttribute("stdDeviation", str(self.blur))
        blur_xml_element.setAttribute("in", "myColorMatrix")
        filter_xml_element.appendChild(blur_xml_element)
        return filter_xml_element