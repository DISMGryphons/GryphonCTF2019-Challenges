# A Certain Scientific Regex

## Question Text
Being greedy for the flag might help here. </br></br>
Creator - ninjassword </br>

### Hints (Optional)
1. Before crossing the road, what do you do? </br>

## Solution
1. Control F for "GCTF{"
2. Inside the fake flag, there is a string, use base64 decode to bring you to the pastebin of https://pastebin.com/TAVE5J94
3. Craft a suitable regex string to capture the strings as required by the challenge. One example is:(?<=Z)([B-D])([I-K]).?\D?\d{3,5}\D?.?\2\1(?!A)
4. Collect these strings in the order by which they appear in the challenge text.
5. Once done head over to the twitter link provided in the pastebin.
6. For each matched string, convert them to ascii values. Then take the sum of these values and look at the last three digits.
These three digits will then be used to convert back into characters by referencing the ascii table.

### Flag
 GCTF{FLaG-4-RG}
