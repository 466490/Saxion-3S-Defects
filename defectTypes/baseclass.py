from abc import ABC, abstractmethod

class BaseClass(ABC):
    classname = "baseclass"
    parameters = {"layer":{"display_name":"Layer","type":"layer", "default": "none"},
                  "density_mean":{"display_name":"Density mean","type":"float","min":0,"max":10e6,"default":3.0},
                  "angle_variance":{"display_name":"Angle variance","type":"percentage", "default":30},
                  "color":{"display_name":"Color","type":"color", "default":"#000000"}}
    
    @classmethod
    def get_classname(cls):
        return cls.classname
    
    @classmethod
    def get_parameters(cls):
        return cls.parameters

    @abstractmethod
    def get_image_dimensions(self):
        pass

    @abstractmethod
    def get_image_binary(self, format, bbox):
        pass

    @abstractmethod
    def get_all_bbox_coords(self):
        pass