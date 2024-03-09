import os
import shutil

def list_files(folder_path, extension=".tif"):
    #List all TIF files in the specified folder.
    tif_files = [file for file in os.listdir(folder_path) if file.endswith(extension)]
    return tif_files

def Copy_to_folders_pan(folder_pan,folder_copy_pan):
    try:
        # Check if the provided path is a directory
        if os.path.isdir(folder_pan):
            # Get tif files of the directory
            tif_files = list_files(folder_pan)
            
            # Print the names of all files
            for file in text_file:
                for pan in tif_files:
                    if pan[:6] == file[:-11]:
                        shutil.copy(os.path.join(folder_pan, pan), os.path.join(folder_copy_pan, pan))
        else:
            print(f"{folder_pan} is not a valid directory.")
    except Exception as e:
        print(f"An error occurred: {e}")

# For Pan folders
#folder_pan = r'C:\Users\dewmi\OneDrive - Fondation EPF\Uni\4eme Année\Project\Images\data_v2\src_pan'
#folder_copy_pan = r'C:\Users\dewmi\OneDrive - Fondation EPF\Uni\4eme Année\Project\Images\data_v2\scr_pan_with_buildings_pv'

#For xs folders
folder_xs = r'C:\Users\dewmi\OneDrive - Fondation EPF\Uni\4eme Année\Project\Images\data_v2\src_xs'
folder_copy_xs = r'C:\Users\dewmi\OneDrive - Fondation EPF\Uni\4eme Année\Project\Images\data_v2\#Sorted_patches_pan_xs\Only Buildings\building_xs'

#Text file with the file names to be moved
text_f = r'C:\Users\dewmi\OneDrive - Fondation EPF\Uni\4eme Année\Project\Images\data_v2\#Sorted_patches_pan_xs\Only Buildings\building.txt'
text_file = open(text_f, 'r')


Copy_to_folders_pan(folder_xs,folder_copy_xs)





