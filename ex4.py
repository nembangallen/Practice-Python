"""
WAP that asks the user for a number and then 
prints out a list of all the divisors of that number. 
"""
inputNum = int(input("Please enter a number: "))
x = range(1,inputNum+1);
for item in x:
    if inputNum % item == 0:
        print(item)

