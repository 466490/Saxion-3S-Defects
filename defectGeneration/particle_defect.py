import math
import shutil
import random
import os.path
import numpy as np
import svgpathtools as svgpt
from svgpathtools.path import bezier_segment
from wand.image import Image
from xml.dom.minidom import parse, parseString

class ParticleDefect():
    def __init__(self, srcImg, area, 
                 density_mean, density_stddev, # defects per 1000x1000 pixels
                 size_mean, size_stddev,
                 angle_mean, angle_stddev,
                 curviness, blur, 
                 layer="none"):
        self.srcImg = srcImg
        self.layer = layer
        self.blur = blur/20
        self._svgDir = ""
        self._svgFilename = ""
        self.defects_bezier_segments = []

        amount_of_defects = self._calculate_amount_of_defects(density_mean, density_stddev, area[2], area[3])

        for defect_index in range(amount_of_defects):
            # Calculate all the angles of the defect, this determines the amount of vertices
            angles = self._calculate_angles(angle_mean, angle_stddev)

            # Choose middle point of defect uniformly on area
            middle_point = self._calculate_middle_point(area)

            defect_points = []

            # Add first defect point to array
            defect_points.append(self._calculate_first_point(size_mean, size_stddev, middle_point))

            # Calculate the rest of the defect points based on the previous one
            for index in range(len(angles)-1):
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
            self.defects_bezier_segments.append(bezier_segments)
    
    def _calculate_angles(self, angle_mean, angle_stddev):
        total_angle = 0
        angles = []
        while total_angle < 360:
            new_angle = np.random.normal(angle_mean, angle_stddev)
            total_angle += (0 if new_angle < 0 else new_angle)
            angles.append(float(new_angle))
        return [360/total_angle*angle for angle in angles]

    def _calculate_amount_of_defects(self, density_mean, density_stddev, width, height):
        # Density is calculated per 1000x1000 pixels
        density_factor = (width*height)/1000000
        density_normal = np.random.normal(density_mean, density_stddev)
        return round((0 if density_normal < 0 else density_normal) * density_factor)
    
    def _calculate_amount_of_vertices(self, vertices_mean, vertices_stddev):
        return round(np.random.normal(vertices_mean, vertices_stddev))
    
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
            cp1_distance = np.abs(points[index-1]-points[index])*(curviness/100)+0.00001
            cp2_distance = np.abs(points[index]-points[next])*(curviness/100)+0.00001

            control_point1 = np.exp(1j*control1_angle) * cp1_distance + points[index]
            control_point2 = np.exp(1j*control2_angle) * cp2_distance + points[index]
            control_points_pairs.append((control_point1, control_point2))
        return control_points_pairs
    
    def get_boundingbox(self):
        x_max, y_max = -10e6, -10e6
        x_min, y_min = 10e6, 10e6
        for point in self.points: # TODO broken
            if point.real > x_max:
                x_max = point.real
            if point.real < x_min:
                x_min = point.real
            if point.imag > y_max:
                y_max = point.imag
            if point.imag < y_min:
                y_min = point.imag
        return (x_min+700, y_min+950, x_max+700, y_max+950)

    def get_image(self):
        svg_out_dir = "output/temp/"
        try:
            self._svgFilename = "temp_large_particle.svg"
            shutil.copyfile(self.srcImg, svg_out_dir+self._svgFilename)
            xmlDoc = parse(svg_out_dir+self._svgFilename)
        except Exception:
            print("The input SVG image is not found or the output directory does not exist")
            return
        
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
        xmlDoc.firstChild.appendChild(filter_xml_element)

        for bezier_segments in self.defects_bezier_segments:
            # Create the XML element as a <path> tag
            defect_xml_element = xmlDoc.createElement("path")
            defect_xml_element.setAttribute("filter", "url(#blur_filter)")
            defect_xml_element.setAttribute("d", svgpt.Path(*bezier_segments).d())
            defect_xml_element.setAttribute("style", "fill:black;fill-opacity:1;stroke:black;none;none")

            if self.layer != "none":
                # Find correct elements based on layer
                for element in xmlDoc.getElementsByTagName("g"):
                    if element.getAttribute("inkscape:label") == self.layer:
                        element.appendChild(defect_xml_element)
            else:
                # Put defect on top of everything
                xmlDoc.firstChild.appendChild(defect_xml_element)

        # Write the changed xml file to disk
        with open(svg_out_dir+self._svgFilename, "w") as file:
            file.write(xmlDoc.toxml())
        self._svgDir = svg_out_dir

        with Image(filename=svg_out_dir+self._svgFilename) as svgImg:
                    png_image = svgImg.make_blob("png32")

        with open(svg_out_dir+self._svgFilename.replace("svg", "png"), "wb") as out:
            out.write(png_image)

        return svg_out_dir+self._svgFilename.replace("svg", "png")

    def output_to_svg(self, svg_out_dir="output/svg/"):
        try:
            self._svgFilename = self._find_available_filename(svg_out_dir, "large_particle%s.svg")
            shutil.copyfile(self.srcImg, svg_out_dir+self._svgFilename)
            xmlDoc = parse(svg_out_dir+self._svgFilename)
        except Exception:
            print("The input SVG image is not found or the output directory does not exist")
            return
        
        # Create the filter element as a <filter>
        filter_xml_element = xmlDoc.createElement("filter")
        filter_xml_element.setAttribute("id", "blur_filter")

        feTurbulence_element = parseString('<feTurbulence type="fractalNoise" result="myComposite" baseFrequency="0.02" numOctaves="5" seed="2" />')
        filter_xml_element.appendChild(feTurbulence_element.documentElement)
        feComposite_element = parseString('<feComposite operator="in" in="myTurbulence" in2="SourceAlpha" result="myComposite"/>')
        filter_xml_element.appendChild(feComposite_element.documentElement)
        feColorMatrix_element = parseString('<feColorMatrix type="myComposite" values="0.012 0 0 0 0  0 0.012 0 0 0  0 0 0.012 0 0  2 2 2 0.9 0"></feColorMatrix>')
        filter_xml_element.appendChild(feColorMatrix_element.documentElement)

        # Create the Gaussian blur element as a <feGaussianBlur> tag
        blur_xml_element = xmlDoc.createElement("feGaussianBlur")
        blur_xml_element.setAttribute("stdDeviation", str(self.blur))
        filter_xml_element.appendChild(blur_xml_element)
        xmlDoc.firstChild.appendChild(filter_xml_element)

        # Create the XML element as a <path> tag
        defect_xml_element = xmlDoc.createElement("path")
        defect_xml_element.setAttribute("filter", "url(#blur_filter)")
        defect_xml_element.setAttribute("d", svgpt.Path(*self.defects_bezier_segments).d())
        defect_xml_element.setAttribute("style", "fill:black;fill-opacity:1;stroke:black;none;none")


        if self.layer != "none":
            # Find correct elements based on layer
            for element in xmlDoc.getElementsByTagName("g"):
                if element.getAttribute("inkscape:label") == self.layer:
                    element.appendChild(defect_xml_element)
        else:
            # Put defect on top of everything
            xmlDoc.firstChild.appendChild(defect_xml_element)

        # Write the changed xml file to disk
        with open(svg_out_dir+self._svgFilename, "w") as file:
            file.write(xmlDoc.toxml())
        self._svgDir = svg_out_dir


    def output_to_csv(self, csv_out_dir="output/csv/"):
        if self._svgFilename == "":
            self.output_to_svg()
        try:
            data_line = "large_particle,"+csv_out_dir+self._svgFilename.replace("svg", "png")+",%.2f,%.2f,%.2f,%.2f"%self.get_boundingbox()+"\n"
            if os.path.exists(csv_out_dir + "large_particle.csv"):
                with open(csv_out_dir + "large_particle.csv", "a") as file:
                    file.write(data_line)
            else:
                with open(csv_out_dir + "large_particle.csv", "w") as file:
                    file.write("class,filename,xmin,ymin,xmax,ymax\n")
                    file.write(data_line)
        except Exception:
            print("Was unable to save the defect to the csv file")

    def output_to_png(self, png_out_dir="output/png/", with_bbox=False):
        if self._svgFilename == "":
            self.output_to_svg()
        try:
            if with_bbox:
                pass #TODO
            else:
                with Image(filename=self._svgDir+self._svgFilename) as svgImg:
                    png_image = svgImg.make_blob("png32")

            with open(png_out_dir+self._svgFilename.replace("svg", "png"), "wb") as out:
                out.write(png_image)
        except Exception as e:
            print(e)
        
    def _find_available_filename(self, search_dir, filename):
        #Runs in log(n) time where n is the number of existing files in sequence
        index = 1
        while os.path.exists(search_dir + filename % index):
            index *= 2

        interval_begin, interval_end = (index // 2, index)
        while interval_begin + 1 < interval_end:
            midpoint = (interval_begin + interval_end) // 2
            interval_begin, interval_end = (midpoint, interval_end) if os.path.exists(search_dir+filename % midpoint) else (interval_begin, midpoint)

        return filename % interval_end