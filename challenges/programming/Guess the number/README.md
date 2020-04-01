# Guess the number
## Question Text

Two of our employees keep sending python scripts to each other. We intercepted one and it just seems to be a simple game. What seems to be the purpose of this?

### Hints (Optional)
1. Multiples of 3


## Solution
1. Change the flag.txt contents from base64 to normal text to view the source code.
2. Create a for loop that appends every value in the dict that contains a multiple of 3 in the key.
3. Print out the final result to get the flag in hex, then convert it to text.

Solution code to be appended to bottom of flag.txt:

for i,v in b:
    if int(i[1::])%3==0:
        c += str(hex(v))[2::]+" "
print(c.strip())

### Flag
`GCTF{1_L0V3_PYTH0N}`

## Recommended Reads
* https://www.base64decode.org/
* https://www.w3schools.com/python/python_dictionaries.asp