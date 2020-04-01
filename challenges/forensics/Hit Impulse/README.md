# Hit Impulse

## Question Text

An insider was found in our company. We found these suspicious files on his desktop. Can you figure out what they contain?

### Hints (Optional)
1. Web traffic may contain more information
2. You might need a shovel for all this SNOW we have.

## Solution
1. Use hex editor on flag.docx and change file to pcapng file.
2. Search through HTTP packets to find the SNOW password.
3. Use SNOW password on iminlovewith.txt.

### Flag
`GCTF{d0ntd0drug$}`

## Recommended Reads
* http://mewbies.com/steganography/snow/how_to_conceal_a_message_in_a_text_file.htm
* https://en.wikipedia.org/wiki/List_of_file_signatures