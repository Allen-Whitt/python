# https://towardsdatascience.com/hiding-data-in-an-image-image-steganography-using-python-e491b68b1372

import cv2
import numpy as numpy
import types
#from google.colab.patches import cv2_imshow

def messageToBinary(message):
    if type(message) == str:
        return ''.join([ format(ord(i), "08b") for i in message ])
    elif type(message) == bytes or type(message) == np.ndarray:
        return [ format(i, "0b8") for i in message ]
    elif type(message) == int or type(message) == np.uint8:
        return format(message, "08b")
    else:
        raise TypeError("Input not supported")

def hideData(image, secret_message):
    n_bytes = image.shape[0] * image.shape[1] * 3
    print("MAX BYTES TO ENCODE: ", n_bytes)
    
    if len(secret_message) > n_bytes:
        raise ValueError("Error: Insufficient bytes to store message")
        
        secret_message += "#####" # Delimiter
        
        data_index = 0
        binary_secret_msg = messageToBinary(secret_message)
        
        data_len = len(binary_secret_msg)
        for values in image:
            for pixel in values:
                r, g, b = messageToBinary(pixel)
                if data_index < data_len:
                    pixel[0] = int(r[:-1] + binary_secret_msg[data_index], 2)
                    data_index += 1
                if data_index < data_len:
                    pixel[1] = int(g[:-1] + binary_secret_msg[data_index],2)
                    data_index += 1
                if data_index < data_len:
                    pixel[2] = int(b[:-1] + binary_secret_msg[data_index],2)
                    data_index += 1
                if data_index >=data_len:
                    break
        print(image)
        return image
        
def showData(image):
    binary_data = ""
    for values in image:
        for pixel in values:
            r, g, b = messageToBinary(pixel)
            binary_data += r[-1]
            binary_data += g[-1]
            binary_data += b[-1]
    all_bytes = [binary_data[i: i+8] for i in range(0, len(binary_data),8)]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte,2))
        if decoded_data[-5:] == "#####" :
            break
    return decoded_data[:-5]
    
def encode_text():
    image_name = input("Enter Image Name (with extension): ")
    image = cv2.imread(image_name)
    
    print("The image is shown below")
    resized_image = cv2.resize(image,(500,500))
    #cv2_imshow(resized_image)
    
    data = input("Enter message to be hidden: ")
    if (len(data)==0):
        raise ValueError("Data is empty")
        
    filename = input("Enter name of new encoded file (with extension): ")
    encoded_image = hideData(image, data)
    print(encoded_image)
    cv2.imwrite(filename, encoded_image)
    
def decode_text():
    image_name = input("Enter the name of the image you want to decode (With extension")
    image - cv2.imread(image_name)
    
    print("The image is as shown below: ")
    resized_image = cv2.resize(image, (500,500))
    #cv2_imshow(resized_image)
    
    text = showData(image)
    return text

def Steganography():
    a = input("Image Steganography \n 1. Encode Data \n 2. Decode Data\n")
    userinput = int(a)
    if(userinput == 1):
        encode_text()
    elif(userinput == 2):
        print(f"Decoded message is {decode_test()}")
    else:
        raise Exception("Enter correct input")
        
Steganography()
