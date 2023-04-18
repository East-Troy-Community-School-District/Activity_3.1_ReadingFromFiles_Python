'''
Programming Languages
Pawelski
4/17/2023
Python II

Instructions:

Part 1:
Let's look at how the project is structured.
Why must all the files be in the same directory
or folder? What is main.py?

Part 2:
Run the program in debugging mode to see how it
works. What happens if you remove "r" from open?
Add the code to the program so that it opens the
file called "random_numbers.txt", reads all the numbers,
and prints them to the console. What is the data
type of the numbers?

Part 3:
Modify the program so that it only reads the first
line of both files. Why might this be difficult
if you don't know how many characters the first line
is?

Part 4:
Modify the program so that it uses the readline()
method to read the first line in each file. What
happens if you call the readline() method again?
'''

languages_file = open("programming_languages.txt", "r")
print(languages_file.read())
languages_file.close()