x = int(input())
num = x
result = 0
while num> 0:
  ld = num%10
  result = result*10 + ld
  num = num//10
print(result == x)

"""Time Complexity is O(log10(n)) and Space Complexity is O(1)"""