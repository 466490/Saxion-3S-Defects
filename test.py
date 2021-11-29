from defectGeneration.defectTypes.largeParticle import LargeParticle

baseImage = "../base_design_V4.svg"
largeParticle = LargeParticle(srcImg=baseImage, 
                              area=(-700, -950, 1400, 1650), 
                              vertices_mean=20, vertices_stddev=2, 
                              size_mean=25, size_stddev=4,
                              distance_mean=1, distance_stddev=0.2,
                              angle_mean=18, angle_stddev=1)
# generate svg file
largeParticle.output_to_svg()

# store in csv file, it will always make sure to generate svg file first
largeParticle.output_to_csv()

# output to png image, it will always make sure to generate svg file first
largeParticle.output_to_png()