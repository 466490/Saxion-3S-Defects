import re
from .attributes import Attributes
from svgpathtools import *
import random
import copy
import numpy as np

class Component(Attributes):

    def __init__(self, paths, attribs) -> None:
        super().__init__(attribs=attribs)
        self.__paths = paths
        self._masks = []
    
    def bbox_full(self):
        max_x = 0
        max_y = 0
        min_x = 10e6
        min_y = 10e6
        for comp in range(len(self.__paths)):
            for line in self.__paths[comp]:
                if(max_x <= max(line.start.real, line.end.real)):
                    max_x = max(line.start.real, line.end.real)

                if(max_y <= max(line.start.imag, line.end.imag)):
                    max_y = max(line.start.imag, line.end.imag)
                
                if(min_x >= min(line.start.real, line.end.real)):
                    min_x = min(line.start.real, line.end.real)
                
                if(min_y >= min(line.start.imag, line.end.imag)):
                    min_y = min(line.start.imag, line.end.imag)
        
        return (max_x, max_y, min_x, min_y)
    
    def return_paths(self):
        return self.__paths
    
    def direction(self, cluster, line):
        S = self.__paths[cluster][line].start
        E = self.__paths[cluster][line].end

        epsilon = 1e-7 # to avoid division by 0

        real_part = (S-E).real
        imag_part = (S-E).imag

        x = round(real_part/abs(real_part + epsilon), 2)
        y = round(imag_part/abs(imag_part + epsilon), 2)

        return x, y
        
    def length(self, cluster, line):
        """Returns:
            (x len, y len)
        """        
        line_start_real = self.__paths[cluster][line].start.real
        line_start_imag = self.__paths[cluster][line].start.imag

        line_end_real = self.__paths[cluster][line].end.real
        line_end_imag = self.__paths[cluster][line].end.imag

        x_len = abs(line_start_real - line_end_real)
        y_len = abs(line_start_imag - line_end_imag)

        return (x_len, y_len)
    
    def clusters(self):
        return len(self.__paths)

    def paths_in_a_cluster(self, line):
        return len(self.__paths[line])

    def random_start_end_line(self, cluster, line=0, len_per=0.05):
        # print(cluster, line)
        xlen, ylen = self.length(cluster, line)
        x_direction, y_direction = self.direction(cluster, line)

        len_percent = len_per
        x_delta = x_direction * (xlen * len_percent) # some scalar 
        y_delta = y_direction * (ylen * len_percent) 

        line_start_real = self.__paths[cluster][line].start.real
        line_start_imag = self.__paths[cluster][line].start.imag

        line_end_real = self.__paths[cluster][line].end.real
        line_end_imag = self.__paths[cluster][line].end.imag

        #TODO: figure out this part lol
        min_error = 5 * (-x_direction)
        y_min_error = 5 * (-y_direction)

        current_line = self.__paths[cluster][line]

        start = complex(random.uniform(line_start_real-x_delta, line_end_real+x_delta)-min_error, \
                        (random.uniform(line_start_imag-y_delta, line_end_imag+y_delta)-y_min_error))  # Random starting point

        defect_point = complex(random.uniform(start.real, start.real-x_delta)+min_error, \
                        (random.uniform(start.imag, start.imag-y_delta)+y_min_error))

        new_line = Line(current_line.start, start)
        new_endline = Line(defect_point, current_line.end)

        return new_line, new_endline
    
    def random_cluster(self):
        return random.randint(0, self.clusters() - 1)

    def get_coords_matrix(self):
        parsed_data = self.get_transform_matrix()
        a, b, c, d, e, f = parsed_data[parsed_data.find("(")+1:parsed_data.find(")")].split(',')

        return np.matrix([[a,c,e], [b,d,f]]).astype(float)

    def override_component(self, data):
        self.__paths = data

    def create_box(min_x, max_x, min_y, max_y):

        _top_left = complex(min_x, max_y)
        _top_right = complex(max_x, max_y)
        _bottom_right = complex(max_x, min_y)
        _bottom_left = complex(min_x, min_y)

        line_1 = Line(_top_left, _top_right)
        line_2 = Line(_top_right, _bottom_right)
        line_3 = Line(_bottom_right, _bottom_left)
        line_4 = Line(_bottom_left, _top_left)

        return Path(line_1, line_2, line_3, line_4)
    
    def append_path(self, path_d):
        self.__paths.append(path_d)

