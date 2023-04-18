'''
Coin Flips
Pawelski
4/17/2023
Python II

Instructions:
What is flips? Why might it be easier to read all the
lines into a list instead of directly from the file?
Why must we use the strip() method?
Modify the program so that it also counts the number
of times tails appears in the file.
'''

file = open("coin_flips.txt", "r")
flips = file.readlines()
file.close()

heads_count = 0
for flip in flips:
    if flip.strip() == "head":
        heads_count += 1
print("Heads:", heads_count)