from .component import Component
from svgpathtools import *
import random
import copy

class MembraneDefect(Component):

    def __init__(self, paths, attribs=None) -> None:
        super().__init__(paths=paths, attribs=attribs)
        self.__defect_coords = []
        self.__defective_membranes = []

    def generate_defects(self, amount=1, sigma=1, size=0.05):
        for i in range(amount):
            copied_layer = copy.deepcopy(self.return_paths())

            random_cluster = self.random_cluster()
            random_line = random.randint(0,len(copied_layer[random_cluster])-1)
            horizontal, vertical = self.direction(random_cluster, random_line)
            line_start, line_end = self.random_start_end_line(random_cluster, random_line, len_per=size)
            
            defect_size = line_start.end - line_end.start


            #TODO: fix this also..
            x_len = defect_size.real
            y_len = defect_size.imag

            # abs(horizontal) - 1 line horizontal / 0 line vertical
            # abs(vertical) - 1 line vertical / 0

            if random.uniform(0, 1) >= 0.5: # whether it goes inside or outside...
                x_min_defect = (abs(vertical) * 10)  * -1
                y_min_defect = (abs(horizontal) * 10) * -1
            else:
                x_min_defect = (abs(vertical) * 10) # if line is vertical, emphasize x
                y_min_defect = (abs(horizontal) * 10) # if line is horizontal, emphasize y
                
            control1_p = complex(random.uniform(line_start.end.real + x_min_defect, line_start.end+(x_min_defect *5) ), \
                            (random.uniform(line_end.start.imag + y_min_defect, line_end.start.imag+(y_min_defect *5 )))) 

            control2_p = complex(random.uniform(control1_p.real, control1_p.real + (x_min_defect * 3)), \
                            (random.uniform(control1_p.imag, control1_p.imag + (y_min_defect *3)))) 

            new_defect = CubicBezier(start=line_start.end, control1=control1_p, control2=control2_p, end=line_end.start)

            copied_layer[0].extend(Path(line_start, line_end, new_defect)) # append defect to copied layer..

            self.__defective_membranes.append(copied_layer) # do i want to do this?

            self.__append_defect_coord(new_defect.bbox())

    def get_defect_coords(self):
        return self.__defect_coords

    def get_defective_membranes(self):
        return self.__defective_membranes

    def __append_defect_coord(self, coord):
        self.__defect_coords.append(coord)
