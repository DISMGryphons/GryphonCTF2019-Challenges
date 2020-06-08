from PIL import Image

flag_img = Image.open('flag.png')
data = list(flag_img.getdata())

# White = 1, Black = 0
binary_string = ''
for i, pixel in enumerate(data):
  colour = pixel[0]
  if i%8 == 0 and i != 0:
    binary_string += ' '
  if colour == 0:
    binary_string += '0'
  elif colour == 255:
    binary_string += '1'

def binary_to_char(binary):
  """Convery binary string to character"""
  return chr(int(binary,2))

binary_array = tuple(binary_string.split(' '))
output = ''.join(map(binary_to_char,binary_array))
print(output)