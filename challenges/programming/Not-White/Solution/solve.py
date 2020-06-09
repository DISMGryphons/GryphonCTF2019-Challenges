from PIL import Image
import json

#open challenge image
im = Image.open('Distrib\\Challenge.PNG','r')

#this is for reference if u want to see what i was thinking of doing
pixel_val = list(im.getdata())

with open('Solution\\RGBA.txt', 'w') as file:
    file.write(json.dumps(pixel_val))

#For changing the (254,254,254,254) to other color to make it visible
i = 0
for x in pixel_val:
    if x != (255,255,255,255):
        pixel_val[i] = (1,1,1,1)
    i += 1     

#can use this to see the difference before and after, to view the challenge image in RGBA
#with open('Solution\\RGBA2.txt', 'w') as file:
#    file.write(json.dumps(pixel_val))


f = open('Solution\\RGBA.txt', 'r')
out = Image.new("RGBA",(199,45))
out.putdata(pixel_val)
out.save('Solution\\Solve.png')
f.close()