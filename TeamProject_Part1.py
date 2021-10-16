## Modules
import matplotlib.pyplot as plt
import numpy as np
## UDFs
def image_importation():
    ## Part 1
    # img_name = input("Enter the name of the file: ")
    img_name = 'Pale_Blue_Dot_Encrypted.tiff'
    
    # Finds the file type based off of name
    end = img_name[img_name.find('.') + 1: len(img_name)]
    
    # Checks file type and converts to numpy array accordingly
    if end == 'jpg':
        img_encrypted = plt.imread(img_name)
    
    elif end == 'png':
        img_encrypted = plt.imread(img_name)
        img_encrypted = (img_encrypted * 255).astype(np.uint8)
    
    elif end == 'tiff':
        img_encrypted = plt.imread(img_name)[:,:,:3]
    
    else:
        raise NameError(f'"{img_name}" is not a valid image file')
    
    # Returns image data
    return img_encrypted
