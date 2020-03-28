# What does these numbers mean?

## Question Text
What are all these random numbers that this program is spitting out?
>Place the answer into the following GCTF{}
Creator - junwei </br>

### Hints (Optional)
1. ascii is key

## Solution
Option 1:
1) we would provide a hint to the key
2) user has to spam the key into the program and retrieve out the 4 parts of the hashed flag
3) the programs spits on a string of ascii dec, so end user has to manually use a ascii table to convert the character one at a time
4) once all 4 of the ascii strings has been converted to the hash format
5) user now has to placed the MD5 hash in the correct sequence and go to a online md5 hash decrypt “compare hash”
e.g. https://www.md5online.org/md5-decrypt.html
Flag would be retrieved.

Option 2:
1) User use jad to decompile the java class file
2) when the user views the jad file the code would be shown
3) user would be able to see the hashed ascii
4) he would still be required to manually match the letters to a ascii table and put the hash into a md5 hash decryptor to retrieve it.


### Flag
 GCTF{y0u6oTm3}
