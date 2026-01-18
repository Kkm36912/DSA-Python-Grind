""" num = int(input()) #Taking input from user
count = 0             #Declaring an empty variable count that will hold the count of integers
while num > 0:     #Loop runs until num == 0
  num = num//10    #retrieving the remaining number
  count += 1       #incrementing the count value by 1
print(count)
"""

"""METHOD 2 USING LOGARITHMIC FUNCTION"""
from math import *
num = int(input())

def countDigits(num):
  return int(log10(num)+1)

print(countDigits(num))


"""Time Complexity is O(log10(n)) and Space Complexity is O(1)"""