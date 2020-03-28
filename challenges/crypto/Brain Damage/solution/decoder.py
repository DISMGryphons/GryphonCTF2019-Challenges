string = open("C:/Users/melod/Desktop/meloGCTF/Brain Damage/braindamage.txt", "r").read()
decoded = ""
validChars = ['-', '.', '>', '<', '+', ',', '[', ']']
for char in string:
    if char in validChars:
        decoded += char
print(decoded)

# https://www.dcode.fr/brainfuck-language
# Decode Base64 here:
# https://www.base64decode.org/
