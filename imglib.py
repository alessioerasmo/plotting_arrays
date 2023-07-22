import numpy as np

def getblackimgRGB(y_size, x_size):
    """ 
    creates a black RGB image of the input size and outs the images
    with the three color channels (Red Green Blue)
    """
    image =  np.zeros((y_size, x_size, 3), dtype='uint8')
    return image, image[:, :, 0], image[:, :, 1], image[:, :, 2]

def getwhiteimgRGB(y_size, x_size):
    """ 
    creates a white RGB image of the input size and outs the images
    with the three color channels (Red Green Blue)
    """
    image = np.zeros((y_size, x_size, 3), dtype='uint8') + 255
    return image, image[:, :, 0], image[:, :, 1], image[:, :, 2]

def getimgRGB(y_size, x_size, red=0, green=0, blue=0):
    """ 
    creates an RGB image of the input size and outs the images
    with the three color channels (Red Green Blue)
    """
    image = np.zeros((y_size, x_size, 3), dtype='uint8')
    
    if (red < 0):
        red = 0
    elif (red > 255):
        red = 255
    if (green < 0):
        green = 0
    elif (green > 255):
        green = 255
    if (blue < 0):
        blue = 0
    elif (blue > 255):
        blue = 255
    
    image[:, :, 0] += red
    image[:, :, 1] += green
    image[:, :, 2] += blue
    return image, image[:, :, 0], image[:, :, 1], image[:, :, 2]
    
