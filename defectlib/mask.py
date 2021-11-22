from svgpathtools.path import *
from .attributes import Attributes # can probably do something fancier with attributes altogether.. but for now is ok

class Mask(Attributes):
    
    def __init__(self, name, area, atribs=None) -> None:
        super().__init__(attribs=atribs)
        self.name = name
        self.area = area

    def append(self):
        pass
        # append path

    def get_coords(self):
        pass
        # for each path, get bounding box

    def create_box(max_x, max_y, min_x, min_y):
        _top_left = complex(min_x, max_y)
        _top_right = complex(max_x, max_y)
        _bottom_right = complex(max_x, min_y)
        _bottom_left = complex(min_x, min_y)

        line_1 = Line(_top_left, _top_right)
        line_2 = Line(_top_right, _bottom_right)
        line_3 = Line(_bottom_right, _bottom_left)
        line_4 = Line(_bottom_left, _top_left)

        return Path(line_1, line_2, line_3, line_4)
    
    def set_fill_opacity(self, opacity):
        return super().set_fill_opacity(opacity)

    def get_fill_opacity(self):
        return_dict = {}
        return_dict['style'] = super().get_fill_opacity()
        return return_dict
    