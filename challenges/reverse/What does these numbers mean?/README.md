# What does these numbers mean?

## Question Text
What are all these random numbers that this program is spitting out?
<hr>
Place the answer into the following GCTF{}
<hr>
<br><br>

### Hints (Optional)
1. gryphons2020 is key

## Solution
Option 1:
1) Key is provided via "hint" to enter into the flag.class program in which once the key has been entered into the program it would return back a random string from an array of 4. "array[3]". 
e.g. "68, 69, 70, 80, 90" these string has a meaning, in which these string are ascii dec codes.
KEY: gryphons2020
2) Once all 4 parts of the strings has been retrieved, user has to arrange the strings in the correct order
3) Convert the ascii numbers into characters and user would get something like the following
e.g. "68, 69, 69, 68" would be converted to "D, E, E, D"
4) Once all has been converted it would form a 32 character MD5 Hash, go to an online MD5 hash decrypter to retrieve out the flag
e.g. https://www.md5online.org/md5-decrypt.html
5) once flag has been retrieved input the flag into the GCTF{} tag and done

Option 2:
1) User types the command "jad java.class" which would create a jad file showing the source code for the flag program
2) Find the array of ascii code
3) Change the ascii code into Characters as shown in the format above
4) Once all has been converted it would form a 32 character MD5 Hash, go to an online MD5 hash decrypter to retrieve out the flag
e.g. https://www.md5online.org/md5-decrypt.html
5) once flag has been retrieved input the flag into the GCTF{} tag and done



### Flag
 GCTF{y0u6oTm3}
