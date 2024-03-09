import rasterio
import numpy as np
from rasterio.plot import show
import os
import shutil


def list_files(folder_path, extension=".tif"):
    #List all TIF files in the specified folder.
    tif_files = [file for file in os.listdir(folder_path) if file.endswith(extension)]
    return tif_files


def max_band_value(tif_files, folder_path, output_txt_file): 
    max_band_red = 0
    max_band_red_file = ''
    max_band_green = 0
    max_band_green_file = ''
    max_band_blue = 0
    max_band_blue_file = ''
    max_band_ir = 0
    max_band_ir_file = ''
    
    with open(output_txt_file, 'w') as txt_file:
        for xs in tif_files:
            with rasterio.open(os.path.join(folder_path, xs)) as src: # Open the dataset using Rasterio
                full_img = src.read()
                img_band = []

                #Reading the bands from the image 
                for band in range(1,src.count+1):
                    img_band.append(src.read(band))

                max_red = max(max(row) for row in img_band[0])
                '''
                max_green = max(max(row) for row in img_band[1])
                max_blue = max(max(row) for row in img_band[2])
                max_ir = max(max(row) for row in img_band[3])'''

                if max_red > max_band_red:
                    max_band_red = max_red
                    max_band_red_file =  xs
                '''
                if max_green > max_band_green:
                    max_band_green = max_green
                    max_band_green_file = xs
                if max_blue > max_band_blue:
                    max_band_blue = max_blue
                    max_band_blue_file = xs
                if max_ir > max_band_ir:
                    max_band_ir = max_ir
                    max_band_ir_file = xs'''

        #Writing to the text file
        txt_file.write(f"Max red band = {max_band_red}" + '\n')
        '''
        txt_file.write(f"Max green band = {max_band_green}" + '\n')
        txt_file.write(f"Max blue band = {max_band_blue}" + '\n')
        txt_file.write(f"Max IR band = {max_band_ir}" + '\n')'''
        

                
folder_path = r"C:\Users\dewmi\OneDrive - Fondation EPF\Uni\4eme Année\Project\Images\data_v2\src_pan"
output_txt_file = r"C:\Users\dewmi\OneDrive - Fondation EPF\Uni\4eme Année\Project\Images\data_v2\#Sorted_patches_pan_xs\Maximum Wavelength or Band\max_bands.txt"

tif_files = list_files(folder_path)
max_band_value(tif_files, folder_path, output_txt_file)
                




