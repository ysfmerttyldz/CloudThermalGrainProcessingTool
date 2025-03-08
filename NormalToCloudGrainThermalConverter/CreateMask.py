import numpy as np
from PIL import Image
import noise
import matplotlib.pyplot as plt
import random

inputs= "Inputs"
outputs = "Outputs"

def Create_Mask(bg_filename,scale = 800,octaves = 5,persistence = 0.7,lacunarity = 2,alpha_multiplier =0.8,gamma_param = 2):
    background = Image.open(inputs+"/"+bg_filename).convert('RGBA')
    width, height = background.size

    random_seed = random.randint(0, 500)
    alpha = np.zeros((height, width), dtype=np.uint8)

    for y in range(height):
        for x in range(width):
            val = noise.pnoise2(
                x / scale,
                y / scale,
                octaves=octaves,
                persistence=persistence,
                lacunarity=lacunarity,
                repeatx=width,
                repeaty=height,
                base=random_seed,
            )
            normalized = (val + 1) / 2.0
            normalized = normalized ** gamma_param
            raw_alpha = normalized * 255 * alpha_multiplier
            raw_alpha = np.clip(raw_alpha, 0, 255)
            alpha[y, x] = int(raw_alpha)

    plt.imsave("Alpha_Mask.png", alpha, cmap='gray')
    print(f"Alpha mask saved as 'Alpha_Mask.png'.")
