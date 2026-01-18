num = int(input())
power = len(str(num))
total_sum = 0
while num > 0:
  ld = num%10
  num= num//10
  total_sum += ld**power
print(total_sum)

"""Time Complexity is O(log10(n)) and Space Complexity is O(1)"""
