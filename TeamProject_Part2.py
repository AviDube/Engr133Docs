## Modules
import numpy as np

## UDF
# Generates Key
def key_generator(img):
    # i_k = input("Enter the initial key string: ")
    i_k = 'COME AND GET YOUR LOVE'
    k_length = len(i_k) - i_k.count(" ")    

    shape = img.shape
    key = np.ones(shape, dtype = np.uint8)
    
    for x in range(len(key)):
        for y in range(len(key[x])):
            key[x][y] = ((x * y) % k_length) * (2 ** 8 // k_length)
            
    return key

# Decrypts image using xor decryption
def xor_decryption(img_encrypted, key):
    img_decrypted = img_encrypted ^ key
    return img_decrypted
