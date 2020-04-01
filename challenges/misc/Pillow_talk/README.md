# Pillow Talk

## Question Text

When I woke up this morning, I realised my friend sent me a very wierd image last night. What could they be talking about?

*Creator - @Wooniety*

### Hints (Optional)
1. When solving a problem, breaking it up bit by bit helps

## Solution
1. Use a python image processing library
    > Pillow works. `pip install Pillow`
2. Get the RGB value of each pixel
3. (0,0,0) = 0 and (255,255,255) = 1
4. String it altogether and convert from binary

### Flag
`GCTF{w0rld_d0M1NaTioN_dr@ws_fUll_C1rcl3}`