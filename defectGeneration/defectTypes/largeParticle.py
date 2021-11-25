import svgpathtools as pt
from threading import Thread
import numpy as np
import random


class LargeParticle():
    def __init__(self, srcImg, layer, vertices, sigma_r, sigma_phi, amount):
        self.srcImg = srcImg
        self.layer = layer
        self.vertices = vertices
        self.sigma_r  = sigma_r
        self.sigma_phi = sigma_phi
        self.amount = amount

        self.__defect_coords = []
        self.__defective_points = []

        self.generateDefect()

    def generateDefect(self):
        pairs = []
        paths = []
        max_x, max_y, min_x, min_y = 700, 700, -700, -950#self.bbox_full() # gets area of an object

        alpha = 360/self.vertices

        # rotation_matrix = np.matrix([[np.cos(alpha),-np.sin(alpha)], [np.sin(alpha),np.cos(alpha)]]) # might not be necessary?

        starting_x = random.uniform(min_x, max_x)
        starting_y = random.uniform(min_y, max_y)

        size_of_bbox = complex(starting_x.real - starting_x.imag, starting_y.real - starting_y.imag)

        orig = complex(starting_x, starting_y) - complex(random.uniform(self.sigma_r, self.sigma_phi * self.sigma_r), random.uniform(self.sigma_r, self.sigma_phi * self.sigma_r)) #origin point for rotations

        point_start = complex(starting_x, starting_y)

        for points in range(self.vertices):
            point_end = self.rotate(alpha, point_start, orig)
            pairs.append((point_start, point_end))
            point_start = self.rotate(alpha, point_start, orig)

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

    def write_svg(self, folder_name='./generated_images/', n_images=1):
        p, a = self.__get_data()

        v_minx, v_miny, v_width, v_height = self.viewbox_dims()

        width = self.__img_width
        height = self.__img_height

        if len(self.__generated_defects) >=1:

            for each_defect in self.__generated_defects.keys(): #TODO does not support multiple type of defects on a single die yet..

                for i in range(len(self.__generated_defects[each_defect])): # looks at the amount of generated defects... happens when .generate_membrane is called

                    p_copy, a_copy = self.__get_adjusted_data(self.__generated_defects, each_defect, i)
                    file_name = folder_name + each_defect + '_' + str(i)
                    self.__write_to_svg(p_copy, a_copy, file_name, width, height, v_minx, v_miny, v_width, v_height, i)
                
                    worker = Thread(target=self.__write_to_png, args=(self.svg_to_png_queue, folder_name))
                    worker.setDaemon(True)
                    self.svg_to_png_queue.put(each_defect + '_' + str(i))
                    worker.start()
        else:
            for i in range(n_images):
                pt.wsvg(paths=p, attributes=a, filename=folder_name + '.svg', dimensions=(width, height), viewbox=(v_minx, v_miny, abs(v_width) + abs(v_width), abs(v_height) + abs(v_height)))
                    # worker = Thread(target=self.__write_to_png, args=(self.svg_to_png_queue, folder_name))
                    # worker.setDaemon(True)
                    # self.svg_to_png_queue.put(each_defect + '_' + str(i))
                    # worker.start()
        self.svg_to_png_queue.join()
