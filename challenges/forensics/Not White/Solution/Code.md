from PIL import Image
import cv 
import cv2
import numpy as np
import json

im = Image.open('Capture.PNG','r')

pixel_val = list(im.getdata())

# with open('test1.txt', 'w') as file:
#     file.write(json.dumps(pixel_val))
i = 0
for x in pixel_val:
    if x != (255,255,255,255):
        pixel_val[i] = (254,254,254,254)
    i += 1     

with open('test1.txt', 'w') as file:
    file.write(json.dumps(pixel_val))

f = open('test1.txt', 'r')
out = Image.new("RGBA",(199,45))
out.putdata(pixel_val)
out.save('hello.png')