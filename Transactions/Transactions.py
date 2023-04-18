'''
Transactions
Pawelski
4/17/2023
Python II

Instructions:
Start by open the "transactions.txt" file and looking
at how the data is formatted. How is the data formatted?
What do you think each file represents?
Next, run the program. What does it do? How does it work?
You may have noticed that there is a blank line between
each entry. Why? Let's modify the program so that it does
not do this.
Finally, let's modify the program so that it counts the
total number of items sold. 
'''

file = open("transactions.txt", "r")
total = 0
for entry in file:
    print(entry)
file.close()