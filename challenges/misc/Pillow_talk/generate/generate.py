import math
from PIL import Image

def toBinary(to_bin):
    """String to Binary"""
    string = ''
    for char in to_bin:
        converted = bin(ord(char))
        converted = converted[:1] + converted[2:]
        if len(converted) < 8:
            converted = '0'*(8-len(converted)) + converted
        string += converted
    return ''.join(string)

def get_dimensions(string):
    """
    Given string and area = len(string), get the dimensions closest to a square.
    return width, height
    """
    string_length = len(string)
    sqrt_length = math.sqrt(string_length)
    if sqrt_length%1 == 0:
        width=height=sqrt_length
    else:
        for i in range(math.ceil(sqrt_length), 1, -1):
            area = string_length
            if area%i == 0:
                if area/i > i:
                    width = int(area/i)
                    height = i
                else:
                    width = i
                    height = int(area/i)
                break
    return width, height

# Flag here
flag = 'GCTF{w0rld_d0M1NaTioN_dr@ws_fUll_C1rcl3}'
flavour_text = open('flavour_text.txt', 'r').read()
binary_flag = toBinary(flavour_text+flag)
width, height = get_dimensions(binary_flag)
print(f"Flag: {flag}\nDimensions: {width}x{height}")

# Make image here
flag_img = Image.new('RGBA', (width,height))
count = 0
while count < width*height:
    for i in range(height):
        for j in range(width):
            if binary_flag[count] == '1':
                colour = 255
            else:
                colour = 0
            flag_img.putpixel((j,i), (colour, colour, colour, 255))
            count += 1
flag_img.save('flag.png')