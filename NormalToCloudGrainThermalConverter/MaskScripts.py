from PIL import Image

def apply(file_name,opacity_factor = 0.9):
    bg = Image.open("Inputs/"+file_name).convert("RGBA")
    cloud_mask = Image.open("Alpha_Mask.png").convert("L")

    cloud_mask = cloud_mask.point(lambda p: int(p * opacity_factor))

    white_layer = Image.new("RGBA", bg.size, (255, 255, 255, 255))
    white_layer.putalpha(cloud_mask)

    result = Image.alpha_composite(bg, white_layer)
    n = file_name.split(".")[0]
    result_name = "Outputs/Cloud/"+n+".png"
    result.save(result_name)
    print(f"Processing completed! '{result_name}' created.")