   ## Modules
import numpy as np
import math as m
import matplotlib.pyplot as plt

## Part imports
import TeamProject_Part1 as p1
import TeamProject_Part2 as p2
import TeamProject_Part3 as p3

## UDFs    
# Main function
def gkern(sig, x, y):
    gauss = (1 / (2 * m.pi * m.pow(sig,2)))
    gauss *= m.exp(-(m.pow(x, 2) + m.pow(y,2)) / (2 * m.pow(sig,2)))    
    return gauss

def main():
    ## Part 1
    img_encrypted = p1.image_importation()
    
    ## Part 2
    print("Starting decryption...")
    key = p2.key_generator(img_encrypted)
    
    img_decrypted = p2.xor_decryption(img_encrypted, key)
    plt.imsave('file_original.tiff', img_decrypted)
    plt.imshow(img_decrypted)
    print("Finished decryption...\n")
    
    ## Part 3
    img_float = img_decrypted.astype(np.float64)    
    
    print("Starting greyscale operation...")
    img_greyscale = p3.greyscale(img_float)
    plt.imshow(img_greyscale, cmap = plt.get_cmap('gray'))
    print("Finished greyscale operation...\n")
    
    sig = 10
    #[[0.0625, 0.125, 0.0625], [0.125, 0.25, 0.125], [0.0625, 0.125, 0.0625]]
    
    kernel = [[gkern(sig, 1, 1), gkern(sig, 0, 1), gkern(sig, 1, 1)], \
              [gkern(sig, 1, 0), gkern(sig, 0, 0), gkern(sig, 1, 0)], \
              [gkern(sig, 1, 1), gkern(sig, 0, 1), gkern(sig, 1, 1)]]
    fraction = np.sum(kernel)
    kernel /= fraction
    
    print('Starting gaussian filtering...')
    img_gaussian = p3.gaussian_filter(img_greyscale, kernel)
    plt.imshow(img_gaussian, cmap = plt.get_cmap('gray'))
    print("Finished gaussian filtering...\n")
    
    gx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    gy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    
    print('Starting edge detection...')
    img_edge = p3.edge_detection(img_gaussian, gx, gy)
    plt.imshow(img_edge, cmap = plt.get_cmap('gray'))
    print("Finished edge detection...\n")
    
    print('Finding Earth...')
    earth_coord = p3.find_earth(img_edge)
    print('Found Earth...')
    print(f'Earth is @{earth_coord}')
    
    img_crop = p3.img_crop(img_decrypted, earth_coord)
    img_crop_edge = p3.img_crop(img_edge, earth_coord)
    
    plt.imshow(img_crop, cmap = plt.get_cmap('gray'))
                                                                        
    plt.imsave('crop.tiff', img_crop)
    plt.imsave('crop_edge.tiff', img_crop_edge, cmap = plt.get_cmap('gray'))
    plt.imsave('img_final.tiff', img_edge, cmap = plt.get_cmap('gray'))

## Calls main function
if __name__ == '__main__':
    main()
