from PIL import Image
import json

#need to open original image and cover it up
im = Image.open('Generate\\Flag.PNG','r')

#this is to list out RGBA of the original image
pixel_val = list(im.getdata())

with open('Generate\\RGBA.txt', 'w') as file:
    file.write(json.dumps(pixel_val))

#For changing the non-white pixel to white
i = 0
for x in pixel_val:
    if x != (255,255,255,255):
        pixel_val[i] = (254,254,254,254)
    i += 1     

#can use this to see the difference before and after, to view the challenge image in RGBA
#with open('Generate\\RGBA2.txt', 'w') as file:
#    file.write(json.dumps(pixel_val))


f = open('Generate\\RGBA.txt', 'r')
out = Image.new("RGBA",(199,45))
out.putdata(pixel_val)
out.save('Generate\\Challenge.png')
f.close()