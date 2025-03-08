import MaskScripts
import CreateMask
import ThermalConverter
import AddGrain

import os
import sys

alpha_multiplier,gamma_param,opacity_factor,grain_intensity = float(sys.argv[1]),float(sys.argv[2]),float(sys.argv[3]),float(sys.argv[4])


input_folder = 'Inputs'
output_folder = 'Outputs'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

print()
print()
print("Hızlı ve Accurate Image Data Thermal Camera, Cloudy, Grainy Image Data Conversion Tool")
print()
print("Processing Images...")
print(f"Alpha multiplier for cloud: {alpha_multiplier}, gamma_param: {gamma_param}, opacity_factor: {opacity_factor}")
print(f"Grain intensity multiplier: {grain_intensity}")
file_names = os.listdir(input_folder)
file_count = len(file_names)
print("Number of Images:",file_count)
print("#####################################################################################################################")
print()
counter = 0

for bg_filename in file_names:
    if bg_filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
        counter+=1
        print(str(counter)+"/"+str(file_count))
        CreateMask.Create_Mask(bg_filename,alpha_multiplier = alpha_multiplier,gamma_param=gamma_param)
        MaskScripts.apply(bg_filename,opacity_factor=opacity_factor)
        ThermalConverter.convert_to_thermal(bg_filename)
        AddGrain.add_film_grain(bg_filename,intensity=grain_intensity)
        print()

print("#####################################################################################################################")
print()
print("Successfully completed! Hızlı ve Accurate.")
