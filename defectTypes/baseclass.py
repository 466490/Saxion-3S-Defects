from abc import ABC, abstractmethod

class BaseClass(ABC):
    # Unique Identifier of the defect
    classname = "baseclass"
    # Parameters for the user to interact with
    parameters = {}

    @classmethod
    def get_classname(cls):
        return cls.classname
    
    @classmethod
    def get_parameters(cls):
        return cls.parameters

    @abstractmethod
    def get_image_dimensions(self):
        # Return a tuple with the width and height of the source image 
        pass

    @abstractmethod
    def get_image_binary(self, format, bbox):
        # Return the generated image in the format svg or png as binary 
        pass

    @abstractmethod
    def get_all_bbox_coords(self):
        # Return a list with the coordinates of all 
        # the bounding boxesaround all defects
        pass


