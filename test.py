import os, sys
import importlib, inspect

files = [f[:-3] for f in os.listdir("defectTypes") if f.endswith('.py') and f != '__init__.py']
for file in files:
    module = importlib.import_module("defectTypes."+file, ".")
    for name, obj in inspect.getmembers(module):
        if inspect.isclass(obj):
            print(obj.get_classname())


# baseImage = "../base_design_V4.svg"

# area = reader.get_area_of_layer(baseImage, "background")

# print(ParticleDefect.get_classname())

# print(ParticleDefect(srcImg=baseImage, area=area,
#                  density_mean=3, density_stddev=1,
#                  size_mean=40, size_stddev=10,
#                  vertices=18, angle_variance=20,
#                  curviness=30, blur=30,
#                  layer="none").get_classname())




