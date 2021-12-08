from xml.dom.minidom import parse

def get_layers(file_path):
    # Parse the SVG file into XML
    xmlDoc = parse(file_path)

    layers = ["none"]
    # Find all the layers based on the attribute "inkscape:groupmode" and the value layer
    for element in xmlDoc.getElementsByTagName("g"):
        if element.getAttribute("inkscape:groupmode") == "layer":
            layers.append(element.getAttribute("inkscape:label"))
    return layers

def get_area_of_layer(file_path, layer):
    # Parse the SVG file into XML
    xmlDoc = parse(file_path)

    area = []
    if layer == "none":
        area_str = xmlDoc.firstChild.getAttribute("viewBox")
        area += [float(area_part) for area_part in area_str.split()]
    else:
        elements = []
        for parent_element in xmlDoc.getElementsByTagName("g"):
            if parent_element.getAttribute("inkscape:label") == layer:
                elements = parent_element.childNodes
        for element in elements:
            if element.nodeName == "rect":
                area += [float(element.getAttribute("x")),
                         float(element.getAttribute("y")),
                         float(element.getAttribute("width")),
                         float(element.getAttribute("height"))]
            elif element.nodeName == "polygon":
                pass #todo
    return area