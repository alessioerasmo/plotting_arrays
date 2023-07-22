from imglib import *

def getimg(arr, Red=None):
    
    line_no = len(arr)
    line_width = 20
    padding = 10

    x_size = (padding+line_width)*line_no + padding

    max_height = int(x_size * 0.75) 

    y_size = max_height

    ( image,red_channel, green_channel, blue_channel ) = getimgRGB(y_size, x_size, 0, 0, 0)

    slice_start = padding
    slice_end = 0

    max = 0
    for i in range(line_no):
        if arr[i] > max:
            max = arr[i]


    for i in range(line_no):
        slice_start += (padding + line_width)*(i>0)
        slice_end = slice_start + line_width + 1
        
        line_height = int((arr[i]/max)*(max_height-padding))            
        
        if (i==Red):
            red_channel[max_height-line_height:max_height-padding, slice_start:slice_end] = 255
            green_channel[max_height-line_height:max_height-padding, slice_start:slice_end] = 0
            blue_channel[max_height-line_height:max_height-padding, slice_start:slice_end] = 0
        else:
            red_channel[max_height-line_height:max_height-padding, slice_start:slice_end] = 255
            green_channel[max_height-line_height:max_height-padding, slice_start:slice_end] = 255
            blue_channel[max_height-line_height:max_height-padding, slice_start:slice_end] = 255
        

    return image