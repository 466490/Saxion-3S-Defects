from defectGeneration.defectTypes.largeParticle import LargeParticle

baseImage = "../base_design_V4.svg"
largeParticle = LargeParticle(srcImg=baseImage, area=(-700, -950, 1400, 1650), vertices=20, sigma_r=25, sigma_phi=4)
# generate svg file
largeParticle.output_to_svg()

# store in csv file, it will always make sure to generate svg file first
largeParticle.output_to_csv()

# output to png image, it will always make sure to generate svg file first
largeParticle.output_to_png()