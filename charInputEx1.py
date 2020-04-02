"""
Create a program that asks the user to enter their name and their age. 
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""
userName = input("Please enter your name: ")
userAge = int(input("Please enter your age: "))
year = str((100-userAge)+2019);
print(userName + " will be 100 years old in the year "+ year)
