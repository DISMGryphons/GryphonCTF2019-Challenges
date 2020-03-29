from random import randint
while True:
    try:
        userin = input("Guess the number!")
        num = randint(0,100000000)
        if userin==num:
            print("Congratulations! You guessed the number. Sadly, the prize isn't the flag.")
        else:
            print("Sorry, that isn't the correct number. The number was "+str(num)+". Try again!")
    except KeyboardInterrupt:
        print("\nThank you for playing. Exiting program.")
        break

a = {
    "a1" : 0x54,
    "a2" : 0x52,
    "a3" : 0x47,
    "a4" : 0x73,
    "a5" : 0x20,
    "a6" : 0x43,
    "a7" : 0x73,
    "a8" : 0x20,
    "a9" : 0x54,
    "a10" : 0x68,
    "b1" : 0x65,
    "b2" : 0x20,
    "b3" : 0x46,
    "b4" : 0x6c,
    "b5" : 0x41,
    "b6" : 0x7b,
    "b7" : 0x4b,
    "b8" : 0x47,
    "b9" : 0x4e,
    "b10" : 0x4a,
    "c1" : 0x20,
    "c2" : 0x58,
    "c3" : 0x31,
    "c4" : 0x43,
    "c5" : 0x6d,
    "c6" : 0x43,
    "c7" : 0x31,
    "c8" : 0x6e,
    "c9" : 0x33,
    "c10" : 0x50,
    "d1" : 0x5a,
    "d2" : 0x6e,
    "d3" : 0x7d,
    "d4" : 0x42
}

b = a.items()
c = ""
# {3, 6, 9} - See the pattern?
for i,v in b:
    if int(i[1::])%3==0:
        c += str(hex(v))[2::]+" "
print(c.strip())