class Attributes():

    def __init__(self, attribs=None) -> None:
        self.__attribs = attribs

        self.__style_fill = 'none' 
        self.__style_fill_opacity = 'none' 
        self.__style_stroke = 'none' 
        self.__style__stroke_opacity = 'none' 
        self.__style_stroke_width = 'none'
        self.__transform = None
        self.__points = None

        if attribs is not None and len(attribs) >= 1:
            try:
                first_atrib = attribs[0]['style'].split(';')
                for style in first_atrib:
                    if 'fill:' in style:
                        # print('true for fill')
                        self.__style_fill = style
                    if 'fill-opacity' in style:
                        # print('true for opacity')
                        self.__style_fill_opacity = style
                    if 'stroke:' in style:
                        # print('true for stroke')
                        self.__style_stroke = style
                    if 'stroke-opacity' in style:
                        self.__style__stroke_opacity = style
                    if 'stroke-width' in style:
                        self.__style_stroke_width = style
            except:
                print('o no, attributes crashed')
            try:
                self.__transform = attribs[0]['transform']
            except:
                pass
            try:
                self.__points = attribs[0]['points']
            except:
                pass

    def return_attribs(self):
        return_dict = {}
        # if len(self.__attribs) >= 1:
        return_dict['style'] = '{};{};{};{};{}'.format(self.__style_fill, self.__style_fill_opacity, self.__style_stroke, self.__style__stroke_opacity, self.__style_stroke_width)
        if self.__transform is not None:
            return_dict['transform'] = '{}'.format(self.__transform)
        if self.__transform is not None:
            return_dict['points'] = '{}'.format(self.__points)
        return return_dict
    
    def get_transform_matrix(self):
        return self.__transform


    def set_fill(self, color):
        """[Set component fill color]

        Args:
            color(HTML color): e.g. #000000, #c00e20 
        """
        self.__style_fill = 'fill:' + str(color)

    def set_fill_opacity(self, opacity):
        """[Set component fill opacity]

        Args:
            color(value): [0,1] value 1 represents 100% opaque
        """
        self.__style_fill_opacity = 'fill-opacity:' + str(opacity)

    def set_stroke(self, color):
        """[Set lines color]

        Args:
            color(HTML color): e.g. #000000, #c00e20 
        """
        self.__style_stroke = 'stroke:' + str(color)
    
    def set_stroke_opacity(self, opacity):
        self.__style_stroke = 'stroke-opacity:' + str(opacity)

    def set_stroke_width(self, width):
        pass #TODO

    def get_fill_opacity(self):
        return self.__style_fill_opacity