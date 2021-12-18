from defectTypes.particle_defect import ParticleDefect
import reader

baseImage = "../base_design_V4.svg"

area = reader.get_area_of_layer(baseImage, "background")
largeParticle = ParticleDefect(srcImg=baseImage, area=area, 
                 density_mean=3, density_stddev=1,
                 size_mean=40, size_stddev=10,
                 vertices=18, angle_variance=20,
                 curviness=30, blur=30, 
                 layer="none")

print(largeParticle.get_boundingbox())
# generate svg file
#largeParticle.output_to_svg()

# store in csv file, it will always make sure to generate svg file first
#largeParticle.output_to_csv()

# output to png image, it will always make sure to generate svg file first
#largeParticle.output_to_png()


