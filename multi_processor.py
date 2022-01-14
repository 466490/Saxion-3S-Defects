import reader
import concurrent.futures

class MultiProcessor():
    def __init__(self, defect_type, parameters):
        self.defect_type = defect_type
        self.parameters = parameters

    def preview_defect(self, mode, bbox):
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = executor.submit(self._run_preview_defect, mode, bbox)
            return results.result()

    def _run_preview_defect(self, mode, bbox):
        defect = self.defect_type(**self.parameters)
        return defect.get_image_binary(mode, bbox)
    
    def _run_gen_and_save_defect(self, defect_type, config, png_dir):
        defect = defect_type(**config)
        png_binary = defect.get_image_binary("png", bbox=False)
        bbox_coords = defect.get_all_bbox_coords()
        width, height = defect.get_image_dimensions()
        available_filename = reader.find_available_filename(png_dir, defect.get_classname()+"%s.png")
        with open(png_dir+available_filename, "w+b") as file:
            file.write(bytearray(png_binary))
        csv_lines = ""
        for bbox in bbox_coords:
            # format of bbox = x_min, y_min, x_max, y_max
            csv_lines += "{},{:.0f},{:.0f},{},{:.6f},{:.6f},{:.6f},{:.6f},\n".format(available_filename,width,height,defect.get_classname(),bbox[1],bbox[0],bbox[3],bbox[2])
        return csv_lines
    
    def gen_defects(self, amount, png_dir, csv_file, progressBar, file_progress):
        csv_lines = ""
        with concurrent.futures.ProcessPoolExecutor() as executor:
            results = [executor.submit(self._run_gen_and_save_defect, self.defect_type, self.parameters, png_dir) for _ in range(amount)]

            for f in concurrent.futures.as_completed(results):
                old_value = progressBar.value()
                progressBar.setValue(old_value+1)
                file_progress.setText(str(old_value+1)+" / " + str(amount))
                csv_lines += f.result()
        with open(csv_file, "a") as file:
            file.write(csv_lines)
        