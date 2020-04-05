# Alphabets

## Question Text
Just a bunch of gibberish but i do remember there should be a way to view it and there should be
a pattern to get the code....

Creator - Pinat

## Hints
What happens if you start ignoring the numbers from 20-29

## Solution:
When you first receive the file u can try to open it with notepad and you'll notice that you've gotten a bunch of gibberish.
Now try opening the file with a hex editor either use notepad++ with the hex editor extention or you could use certain linux distribution such as kali that has a hex editor by default.

After opening it in the hexeditor the bunch of numbers and signs are meant to confuse u. Start by looking at the number from the top left if you happen to be using the same hex editor as me u should see 05.The hint given in the file that comes with the challenge is that there are no 20s and that is what u should be doing. Ignoring all the numbers from 20 to 29 u should obtain in this order from left the right
[05 30 09 46 41 18 45] Compare the numbers to the one in the txt file that came with the challenge u should get the flag

## Flag
GCTF{EdItoRs}
