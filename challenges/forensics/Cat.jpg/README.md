# Cat.jpg
## I discovered a cat and it handled me a note.
## It says to use steghide to extract and a key was given: unlock 
## I can use this key to find more clues... 

**Hint**
1. The cat passed me another note, it says hex editor and file signature.
## Distribution
- cat.jpg
- SHA1: CF6F0343B001F405AA61102DF5F936BC32D0BEEC
## Solution
use steghide. steghide extract -sf cat.jpg
when asked for the passphrase, use unlock
you will receive a zip file. Navigate the zip file till you find a pdf name cat.pdf
retrieve it and you can view it. Use a hex editor to carve out a PNG image of the flag from the PDF.
**Flag**

`GCTF{m30w_y0u_g0t_m3}`
## Recommended Reads
https://www.garykessler.net/library/file_sigs.html
