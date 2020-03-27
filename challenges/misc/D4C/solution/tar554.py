import os
y = 554
for x in range(0,554,1):
    os.system('tar -xvf '+ str(bin(y)) +'.tar.gz')
    os.remove(str(bin(y))+'.tar.gz')
    y = y-1
