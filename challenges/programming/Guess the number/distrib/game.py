import base64
f = open("flag.txt")
fr = f.read()
eval(compile(base64.b64decode(fr),"string","exec"))
