import re
import numpy as np
from svgpathtools.path import translate
from threading import Thread
from .component import Component
from svgpathtools import wsvg
from wand.image import Image

from .membrane import MembraneDefect
from .particles import Particles
import os
from queue import Queue
import time
import copy
import math

from defectlib import membrane
from defectlib import component
import pandas as pd


class Die():
    svg_to_png_queue = Queue(maxsize=100)

    def __init__(self, device_paths, device_attributes, a, b, c, d, width=768, height=960) -> None:
        self._components = {}
        self.__generated_defects = {}
        self.__defects_csv = {}
        self.__img_width = width
        self.__img_height = height
        self.view1 = a
        self.view2 = b
        self.view3 = c
        self.view4 = d

        if device_paths is not None:
            try:
                for each_component in device_paths.keys():
                    self._components[each_component] = Component(device_paths[each_component], device_attributes[each_component])
            except:
                print('die crashed')
    
    def add_component(self, component_name, component, atribs=None):
        self._components[component_name] = (Component(component, atribs))

    def all_components(self):
        return self._components.keys()

    def __get_data(self):
        all_paths = []
        all_attributes = []

        for component in self._components.keys():
            all_paths.extend(self._components[component].return_paths())
            for m_attribs in range(len(self._components[component].return_paths())):
                all_attributes.append(self._components[component].return_attribs())
        
        return all_paths, all_attributes

    def __get_adjusted_data(self, defect_dict, comp, id):
        all_paths = []
        all_atribs = []
        copied_components = copy.deepcopy(self._components)
#
        # for each_defect in defect_dict.keys():
        copied_components[comp].override_component(defect_dict[comp][id])
            # print(defect_dict[each_defect][id])
            # print(copied_components[each_defect].return_attribs())

        for component in copied_components.keys():
            all_paths.extend(copied_components[component].return_paths())
            for m_attribs in range(len(copied_components[component].return_paths())):
                all_atribs.append(copied_components[component].return_attribs())
                
        return all_paths, all_atribs
            

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
                wsvg(paths=p, attributes=a, filename=folder_name + '.svg', dimensions=(width, height), viewbox=(v_minx, v_miny, abs(v_width) + abs(v_width), abs(v_height) + abs(v_height)))
                    # worker = Thread(target=self.__write_to_png, args=(self.svg_to_png_queue, folder_name))
                    # worker.setDaemon(True)
                    # self.svg_to_png_queue.put(each_defect + '_' + str(i))
                    # worker.start()
        self.svg_to_png_queue.join()
    
    def __write_to_svg(self, p, a, name, width, height, v_minx, v_miny, v_width, v_height, iter_):
        wsvg(paths=p, attributes=a, filename=name + '.svg', dimensions=(width, height), viewbox=(v_minx, v_miny, (v_width), (v_height)))
    

    def __write_to_png(self,svg_to_png_queue, folder_name):

        if not os.path.exists(folder_name + 'png/'):
                os.makedirs(folder_name + 'png/')

        while not svg_to_png_queue.empty():
            file_name = svg_to_png_queue.get()
            with Image(filename=folder_name + file_name + '.svg') as image:
                image.save(filename=folder_name + 'png/' + str(file_name) +'.png')
            svg_to_png_queue.task_done()

    def delete_component(self, name):
        try:
            del self._components[name]
        except:
            print('component delete crashed')

        return self._components
    
    def viewbox_dims(self):
        #TODO fixing this would be very helpful...
        v_minx = v_miny = v_maxx = v_maxy = 0
        # (v_minx, v_miny, v_maxx, v_maxy) = self._components['background'].bbox_full()
        # for comp in self._components.keys():
        #     max_x, max_y, min_x, min_y = self._components[comp].bbox_full()

        #     # a_max, b_max = self.translate_defect_coords(self._components[comp], max_x, max_y)
        #     # a_min, b_min = self.translate_defect_coords(self._components[comp], min_x, min_y)
        #     v_minx = min(min_x, v_minx)
        #     v_miny = min(min_y, v_miny)
        #     v_maxx = max(max_x, v_maxx)
        #     v_maxy = max(max_y, v_maxy)
            # v_minx = min(a_min, v_minx)
            # v_miny = min(b_min, v_miny)
            # v_maxx = max(a_max, v_maxx)
            # v_maxy = max(b_max, v_maxy)

        # return (-600, -850, 1225, 1450)
        return (self.view1, self.view2, self.view3, self.view4)
        
    def generate_membrane(self, component='membrane', amount=1, size=0.2):
        die = MembraneDefect(self._components[component].return_paths())
        die.generate_defects(amount,size=size)
        self.__generated_defects[component] = die.get_defective_membranes()
        self.__membrane_defects_coords = die.get_defect_coords() #xmin, xmax, ymin, ymax
    
    def generate_membrane_csv(self):
        v_minx, v_miny, width, height = self.viewbox_dims()

        scale_x = self.__img_width/width
        scale_y = self.__img_height/height
        defects = []

        for i in range(len(self.__membrane_defects_coords)):
            xmin, xmax, ymin, ymax = self.__membrane_defects_coords[i]
            new_x, new_y = self.translate_defect_coords(self._components['membrane'], xmin, ymax)
                                # viewbox xmin... viewbox ymin...
            new_xmin = math.floor(abs(-v_minx - new_x) * (scale_x) )
            new_ymin = math.floor(abs(-v_miny - new_y) * (scale_y) )

            d_width = math.floor(abs((xmax - xmin)) * (scale_x))
            d_height = math.floor(abs((ymax - ymin)) * (scale_y))

            new_xmax = new_xmin + d_width
            new_ymax = new_ymin + d_height

            defects.append(['membrane_' + str(i)+ '.png', self.__img_width, self.__img_height, 'membrane', new_ymin*0.98, new_xmin*0.98, new_ymax*1.03, new_xmax*1.03])
        self.__defects_csv['membrane'] = defects
        return self.__defects_csv
        # getting defects..

    def generate_particles(self, component, n, sigma_r, sigma_phi, amount):
        die = Particles(self._components[component].return_paths())
        die.polygon_points(n, sigma_r, sigma_phi, amount)

        self.add_component('particles', die.get_polygons()[0])

        self._components['particles'].set_fill('black')
        self._components['particles'].set_fill_opacity('1')
        self._components['particles'].set_stroke_opacity(1)
        self._components['particles'].set_stroke('black')

        self.__generated_defects['particles'] = die.get_polygons()
        
        self.__particle_coords = die.get_coords()


    def generate_particles_csv(self):
        v_minx, v_miny, width, height = self.viewbox_dims()

        scale_x = self.__img_width/width
        scale_y = self.__img_height/height


        defects = []
        for i in range(len(self.__particle_coords)):
            xmin, xmax, ymin, ymax = self.__particle_coords[i]
            new_x, new_y = self.translate_defect_coords(self._components['particles'], xmin, ymin)

            new_xmin = (abs(-v_minx + new_x) * (scale_x) )
            new_ymin = (abs(-v_miny + new_y) * (scale_y) )

            d_width = math.floor(abs((xmax - xmin)) * (scale_x))
            d_height = math.floor(abs((ymax - ymin)) * (scale_y))

            
            new_xmax = new_xmin + d_width
            new_ymax = new_ymin + d_height
            defects.append(['particles_' + str(i)+ '.png', self.__img_width, self.__img_height, 'particles', new_ymin*0.98, new_xmin*0.98, new_ymax*1.03, new_xmax*1.03])

        self.__defects_csv['particles'] = defects

        return self.__defects_csv

    def translate_defect_coords(self, component_, x, y):
        try:
            # translation_matrix = self._components['membrane'].get_coords_matrix()
            translation_matrix = component_.get_coords_matrix()

            new_x = np.dot(translation_matrix[0], [float(-x), float(-y), -1])
            new_y = np.dot(translation_matrix[1], [float(-x), float(-y), -1])
            return new_x, new_y
        except:
            # print('returned raw')
            return x, y
    
    def write_complete_csv(self, comp):
        pd.DataFrame(self.__defects_csv[comp], columns=['filename', 'width', 'height', 'class', 'ymin', 'xmin', 'ymax', 'xmax']).to_csv(comp + '.csv', index=False)
    


        

