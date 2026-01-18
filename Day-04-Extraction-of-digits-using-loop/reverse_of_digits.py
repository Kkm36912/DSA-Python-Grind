num = int(input()) #Taking input from user
n = ""             #Declaring an empty string in order to store the reversed number
while num > 0:     #Loop runs until num == 0
  last_digit = num%10  #storing the last digit
  num = num//10        #retrieving the remaining number
  n += str(last_digit) #adding the last digit at the front
print(int(n))