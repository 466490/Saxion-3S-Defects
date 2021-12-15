import concurrent.futures
import queue
from particle_defect import ParticleDefect
import reader
import os

class MultiProcessor():
    def __init__(self, type, config, amount, png_dir, csv_file):
        self.type = type
        self.config = config
        self.amount = amount
        self.png_dir = png_dir
        self.csv_file = csv_file
    
    def gen_defect(self, type, config, png_dir):
        defect = type(*config)
        png_binary = defect.preview_image_png(bbox=False)
        bbox_coords = defect.get_all_bbox_coords()
        available_filename = reader.find_available_filename(png_dir, defect.get_classname()+"%s.png")
        with open(png_dir+available_filename, "w+b") as file:
            file.write(bytearray(png_binary))
        csv_lines = ""
        for bbox in bbox_coords:
            csv_lines += defect.get_classname()+","+available_filename+",%.2f,%.2f,%.2f,%.2f"%bbox+"\n"
        return csv_lines
    
    def run(self, progressBar):
        csv_lines = ""
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(self.gen_defect, self.type, self.config, self.png_dir) for _ in range(self.amount)]

            for f in concurrent.futures.as_completed(results):
                old_value = progressBar.value()
                progressBar.setValue(old_value+1)
                csv_lines += f.result()
        with open(self.csv_file, "a") as file:
            file.write(csv_lines)
        