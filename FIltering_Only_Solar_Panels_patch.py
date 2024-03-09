import rasterio
import os
import shutil

def list_files(folder_path, extension=".tif"):
    #List all TIF files in the specified folder.
    tif_files = [file for file in os.listdir(folder_path) if file.endswith(extension)]
    return tif_files

def contain_buildings_pv(tif_files, folder_path, output_txt_file, output_folder): 
    
    with open(output_txt_file, 'w') as txt_file:
         for patch in tif_files:
             with rasterio.open(os.path.join(folder_path, patch)) as src: # Open the dataset using Rasterio
                 data = src.read(1) 
                 if (2 in data) and (1 not in data):
                     txt_file.write(patch + '\n')
                     shutil.copy(os.path.join(folder_path, patch), os.path.join(output_folder, patch))

    

folder_path = r"C:\Users\dewmi\OneDrive - Fondation EPF\Uni\4eme Année\Project\Images\data_v2\labeled_patches"
output_txt_file = r"C:\Users\dewmi\OneDrive - Fondation EPF\Uni\4eme Année\Project\Images\data_v2\#Sorted_patches_pan_xs\Only Solar Panels\pv.txt"
output_folder = r"C:\Users\dewmi\OneDrive - Fondation EPF\Uni\4eme Année\Project\Images\data_v2\#Sorted_patches_pan_xs\Only Solar Panels\pv_patches"

tif_files = list_files(folder_path)
contain_buildings_pv(tif_files, folder_path, output_txt_file, output_folder)

