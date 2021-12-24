import os
from xml.dom.minidom import parse
from multiprocessing import Lock

mutex = Lock() 
def find_available_filename(search_dir, filename):
    with mutex:
        #Runs in log(n) time where n is the number of existing files in sequence
        index = 1
        while os.path.exists(search_dir + filename % index):
            index *= 2

        interval_begin, interval_end = (index // 2, index)
        while interval_begin + 1 < interval_end:
            midpoint = (interval_begin + interval_end) // 2
            interval_begin, interval_end = (midpoint, interval_end) if os.path.exists(search_dir+filename % midpoint) else (interval_begin, midpoint)

        return filename % interval_end

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
    if layer == "none" or layer == "":
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

def get_first_csv_file(csv_dir, default_filename="train_labels.csv"):
    results = [each for each in os.listdir(csv_dir) if each.endswith(".csv")]
    if not results:
        with open(csv_dir+default_filename, "w") as file:
            file.write("filename,width,height,class,ymin,xmin,ymax,xmax,\n")
        return csv_dir+default_filename
    return csv_dir+results[0]