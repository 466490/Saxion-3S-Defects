import numpy as np
from .component import Component
import svgpathtools as pt
import random

class LParticles(Component):

    def __init__(self, paths, attribs=None) -> None:
        super().__init__(paths, attribs)
    
        self.__defect_coords = []
        self.__defective_points = []

    def polygon_points(self, n_polygon_points, sigma_r, sigma_phi, amount=1):

        for i in range(amount):

            pairs = []
            paths = []
            max_x, max_y, min_x, min_y = self.bbox_full() # gets area of an object

            alpha = 360/n_polygon_points
            dividers = sorted(random.sample(range(1, 360), n_polygon_points - 1))
            alphaArray = [a - b for a, b in zip(dividers + [360], [0] + dividers)]
            print(alphaArray)

            # rotation_matrix = np.matrix([[np.cos(alpha),-np.sin(alpha)], [np.sin(alpha),np.cos(alpha)]]) # might not be necessary?

            starting_x = random.uniform(min_x, max_x)
            starting_y = random.uniform(min_y, max_y)

            size_of_bbox = complex(starting_x.real - starting_x.imag, starting_y.real - starting_y.imag)

            orig = complex(starting_x, starting_y) - complex(random.uniform(sigma_r, sigma_phi * sigma_r), random.uniform(sigma_r, sigma_phi * sigma_r)) #origin point for rotations

            point_start = complex(starting_x, starting_y)

            for points in range(n_polygon_points):
                point_end = self.rotate(alphaArray[points], point_start, orig)
                pairs.append((point_start, point_end))
                point_start = self.rotate(alphaArray[points], point_start, orig)

            for connect_points in pairs:
                paths.append(pt.Line(connect_points[0],connect_points[1]))
            self.__defect_coords.append(pt.Path(*paths).bbox())
            self.__defective_points.append([pt.Path(*paths)])


    def rotate(self, deg, point, origin):
        return np.exp(1j*np.radians(deg))*(point - origin) + origin

    def get_coords(self):
        return self.__defect_coords

    def get_polygons(self):
        return self.__defective_points
    



