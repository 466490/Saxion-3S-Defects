from defectGeneration.defectTypes.largeParticle import LargeParticle

baseImage = "../base_design_V4.svg"
largeParticle = LargeParticle(srcImg=baseImage, 
                              area=(-700, -950, 1400, 1650), 
                              vertices_mean=18, vertices_stddev=2, 
                              size_mean=35, size_stddev=7,
                              angle_variance=10, blur_stddev=1, 
                              curviness=4)
# generate svg file
largeParticle.output_to_svg()

# store in csv file, it will always make sure to generate svg file first
largeParticle.output_to_csv()

# output to png image, it will always make sure to generate svg file first
largeParticle.output_to_png()