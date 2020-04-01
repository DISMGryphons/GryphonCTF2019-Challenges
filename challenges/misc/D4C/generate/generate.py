import os

os.system('tar -czvf '+str(bin(1))+'.tar.gz search.pptx hint.txt')

for x in range (2,555):
    os.system('tar -czvf '+str(bin(x))+'.tar.gz '+str(bin(x-1))+'.tar.gz fill.txt')
    os.remove(str(bin(x-1))+'.tar.gz')
