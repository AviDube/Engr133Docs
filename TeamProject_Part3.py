## Modules      
import numpy as np
from scipy import ndimage
import matplotlib.pyplot as plt
import math as m 

## UDFs
def greyscale(img):
    g = [0.299, 0.587, 0.114]
    img_greyscale = np.dot(img[...,:3], g)
    
    return img_greyscale

def gaussian_filter(img, k):
    img_gaussian = np.ones((img.shape[0], img.shape[1]), dtype = np.float64)
    t = np.ones((3,3), dtype = np.float64)

    img = np.pad(img, 1, mode = 'constant')
    
    for x in range(1, len(img) - 1):
        if x  == ((len(img) - 1) // 4):
            print('. . . 25% COMPLETE')
        
        elif x == ((len(img) - 1) // 2):
            print('. . . 50% COMPLETE')
        
        elif x == (((len(img) - 1) // 4) * 3):
            print('. . . 75% COMPLETE')
       
        elif x == (len(img) - 2):
            print('. . . 100% COMPLETE')
            
        for y in range(1, len(img[x]) - 1):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    t[i + 1, j + 1] = img[x + i, y + j]
                        
            d = np.dot(t, k)
            s = np.sum(d)
            img_gaussian[x-1, y-1] = s   

    return img_gaussian
    
    # return ndimage.gaussian_filter(img, sigma = 1.056)
    
def edge_detection(img, Gx, Gy):
    [rows, columns] = np.shape(img) 
    img_edge = np.zeros((rows, columns), dtype = np.float64)  

    # Now we "sweep" the image in both x and y directions and compute the output
    for i in range(rows - 2):
        if i  == ((rows - 2) // 4):
            print('. . . 25% COMPLETE')
        
        elif i == ((rows - 2) // 2):
            print('. . . 50% COMPLETE')
        
        elif i == (((rows - 2) // 4) * 3):
            print('. . . 75% COMPLETE')
       
        elif i == (rows - 3):
            print('. . . 100% COMPLETE')
            
        for j in range(columns - 2):
            gx = np.sum(np.multiply(Gx, img[i:i + 3, j:j + 3]))  # x direction
            gy = np.sum(np.multiply(Gy, img[i:i + 3, j:j + 3]))  # y direction
            
            if np.hypot(gx, gy) > 250 or np.hypot(gx, gy) == 1:    
                img_edge[i + 1, j + 1] = 255
                
            else:
                img_edge[i + 1, j + 1] = 0
                
    return img_edge
    
def find_earth(img):
    coord = (0, 0) 
    
    t = np.ones((3,3), dtype = np.float64)
    final = np.ones((101,101), dtype = np.float64)
    
    for x in range(1, len(img) - 1):  
        for y in range(1, len(img[x]) - 1):
            for i in range(-1, 2):
                for j in range(-1, 2):
                    t[i + 1, j + 1] = img[x + i, y + j]
                
            if t[1][1] == 0 and np.sum(t) == (255 * 8):
                # img[x][y] = 255
                coord = (x, y)
                return coord                      
                    
def img_crop(img, coord):
    img_cropped = img[(coord[0] - 50):(coord[0] + 51), (coord[1] - 50):(coord[1] + 51)]         
    return img_cropped
                    
                    
                    
                    