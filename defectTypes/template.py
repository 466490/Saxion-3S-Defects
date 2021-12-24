import math
import random
import numpy as np
import svgpathtools as svgpt
import wand.image
from xml.dom.minidom import parse, parseString
import reader

class Defect():
    classname = "template"
    parameters = {"layer":{"display_name":"Layer","type":"layer"},
                  "density_mean":{"display_name":"Density mean","type":"float","min":0,"max":10e6,"default":3.0},
                  "angle_variance":{"display_name":"Angle variance","type":"percentage", "default":30},
                  "color":{"display_name":"Color","type":"color", "default":"#000000"}}
    
    @classmethod
    def get_classname(cls):
        return cls.classname
    
    @classmethod
    def get_parameters(cls):
        return cls.parameters