# inputNum = int(input("Please enter a number: "))
# if inputNum % 2 == 0 and inputNum % 4 == 0:
#     print("Entered number is a multiple of 4.")
# elif inputNum % 2 == 0:
#     print("You have entered an even number.")
# else:
#     print("You have entered an odd number.")

# meal_cost = float(input(12.00))
# print(meal_cost)
#!/bin/python3

import math
import os
import random
import re
import sys
__name__ = "__main__"

# Complete the solve function below.
def solve(meal_cost, tip_percent, tax_percent):
    tip = meal_cost * tip_percent/100
    tax = meal_cost * tax_percent/100
    totalCost = round(meal_cost+tip+tax)
    return totalCost

if __name__ == '__main__':
    meal_cost = float(input())
    tip_percent = int(input())
    tax_percent = int(input())
    solve(meal_cost, tip_percent, tax_percent)
