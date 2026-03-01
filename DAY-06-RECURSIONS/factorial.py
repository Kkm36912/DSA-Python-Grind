# FUNCTIONAL RECURSION
"""n = int(input())
def fact(n):
  if n == 1 or num == 0:
    return 1
  return n*fact(n-1)

factorial = fact(n)
print("The factorial is:",factorial)"""

# PARAMETERIZED RECURSION
n = int(input())
def fact(factorial,i,n):
  if n == 0:
    print("The factorial of given number is: ",factorial)
    return 1
  fact(factorial*i, i+1, n-1)

x = fact(1,1,n)
