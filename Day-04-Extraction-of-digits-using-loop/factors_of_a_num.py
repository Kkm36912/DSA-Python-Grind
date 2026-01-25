"""
*****Brute Force method******
for i in range(1,num+1) 
TC-> O(N)

*******More Optimal*****

for i in range(1,int(num/2))
TC-> O(N/2) approx = O(N)
"""
"""Last Optimal Solution"""
from math import sqrt
num = int(input())
factors = []
for i in range(1, int(sqrt(num))+1):
  if num%i == 0:
    factors.append(i)
    if num//i != i:
      factors.append(num//i)
print(sorted(factors))   #O(NlogN) is TC of Sorted Array

""" TC-> O(sqrt(N))+O(NlogN) """

""" SC-> O(k) """