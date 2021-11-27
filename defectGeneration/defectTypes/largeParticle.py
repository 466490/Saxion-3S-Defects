import shutil
import numpy as np
import random
from xml.dom.minidom import parse


class LargeParticle():
    def __init__(self, srcImg, area, vertices, sigma_r, sigma_phi, layer="none"):
        self.srcImg = srcImg
        self.layer = layer
        self.points = []

        # Uniformly distributed
        dividers = sorted(random.sample(range(1, 360), vertices - 1))
        alphaArray = [a - b for a, b in zip(dividers + [360], [0] + dividers)]

        starting_x = random.uniform(area[0], area[2]+area[0]) # minX, maxX
        starting_y = random.uniform(area[1], area[3]+area[1]) # minY, maxY

        #origin point for rotations
        origin = complex(starting_x, starting_y) - complex(random.uniform(sigma_r, sigma_phi * sigma_r), 
                                                         random.uniform(sigma_r, sigma_phi * sigma_r))

        point_start = complex(starting_x, starting_y)
        self.points.append(point_start)

        for index in range(vertices):
            point_end = self.rotate(alphaArray[index], point_start, origin)
            self.points.append(point_end)
            point_start = self.rotate(alphaArray[index], point_start, origin)

    def rotate(self, deg, point, origin):
        return np.exp(1j*np.radians(deg))*(point - origin) + origin

    def output_to_svg(self, directory):
        #print(self.points)
        shutil.copyfile(self.srcImg, directory + "particle.svg") # check if success
        xmlDoc = parse(directory + "particle.svg")

        # Create defect xml element
        defectElement = xmlDoc.createElement("path")
        pointsStr = ""
        for index, points in enumerate(self.points):
            if index == 0:
                pointsStr += "M " + str(points.real) + "," + str(points.imag)
            else:
                pointsStr += " L " + str(points.real) + "," + str(points.imag)
        defectElement.setAttribute("d", pointsStr)
        defectElement.setAttribute("style", "fill:black;fill-opacity:1;stroke:black;none;none")

        if self.layer != "none":
            # Find correct elements based on layer
            for element in xmlDoc.getElementsByTagName("g"):
                if element.getAttribute("inkscape:label") == self.layer:
                    element.appendChild(defectElement)
        else:
            # Put defect on top of everything
            xmlDoc.firstChild.appendChild(defectElement)

        # Write the changed xml file to disk
        with open(directory + "particle.svg", "w") as file:
            file.write(xmlDoc.toxml())
            file.close()

    def get_boundingbox(self):
        max_x, max_y = -10e6, -10e6
        min_x, min_y = 10e6, 10e6
        for point in self.points:
            if point.real > max_x:
                max_x = point.real
            if point.real < min_x:
                min_x = point.real
            if point.imag > max_y:
                max_y = point.imag
            if point.imag < min_y:
                min_y = point.imag
        return (min_x, min_y, max_x, max_y)