# Untitled Goose Chase

##  Question Text
The goose has stolen and hidden the flag away! Can you find the flag? </br></br>
Creator - @piconjoz

### Hints (Optional)
1.  Look at the words carefully (Riddle 1)
2.  Look deeper into the image (Riddle 2)
3.  Focus on the drawing on the flag (Riddle 3) </br>

## Solution
1.  Unzip goose.zip. Each riddle has an accompanying image that hints what to do with each riddle. For the first riddle, we need to use playfair cipher.
2.  The key is 'goose' as shown in the image. Using this key in an online playfair will yield a hint to solving the next riddle.
3.  The cipher hinted in the previous riddle is the vigenère cipher. To solve riddle 2, we have to understand 2 things from the image; We need to use 2 ciphers in a row to get our riddle solved and we need to change our key from 'goose' to 'loose' (from inspecting properties of the image).
4.  Run riddle 2 text into a vigenère decoder with the key 'loose', and run it through a playfair decoder with 'loose' as the key as well. Now we will get the hint to solve riddle 3.
5.  The additional cipher stated in riddle 2 is the classic Caesar cipher. To solve riddle 3, we need to use what we know from previous the riddles.
6.  We need to get the keys for each cipher. From the drawing, we know that Caesar cipher will use 7, and vigenère will use 'honk' (The recurring sound the goose is shown to make). To get the last key, we also need to inspect the properties of image to get the hint '2=3'. From that, we know that playfair also uses the key 'honk'.
7.  Using the drawing on the flag, put riddle 3 text into each of the ciphers accordingly; Caesar, vigenère and playfair with each corresponding key. </br>

### Flag
> $GCTF{pl4yf41r_v163n3re_c43s4r_y0u_w4573d_y0ur_71m3_7h4nk5_go05e}
