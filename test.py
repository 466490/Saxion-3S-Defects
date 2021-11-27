from defectGeneration.defectTypes.largeParticle import LargeParticle

baseImage = "../base_design_V4.svg"
largeParticle = LargeParticle(srcImg=baseImage, area=(-700, -950, 1400, 1650), vertices=12, sigma_r=16, sigma_phi=4)
largeParticle.output_to_svg("generated_images/svg/")
print(largeParticle.get_boundingbox())