# PARAMETERIZED RECURSION
''' fruits= ['apple', 'mango', 'orange', 'banana', 2, 4, 8, {3,7,29}]
rev_arr = []
length = len(fruits)
def rev(back_index):
  if back_index == 0:
    rev_arr.append(fruits[back_index])
    print(rev_arr)
    return
  rev_arr.append(fruits[back_index])
  rev(back_index-1)

rev(length-1) '''

#USING TWO POINTERS CONCEPT

fruits= ['apple', 'mango', 'orange', 'banana', 2, 4, 8, {3,7,29}]

left = 0
right = len(fruits)-1

def rev(left,right,arr):
  if left >= right:
    #print (arr) will also give the same result then don't return anything with return
    return arr
  arr[left], arr[right] = arr[right], arr[left]
  return rev(left+1, right-1, arr)

#If used print inside if already just simply call the rev()
print(rev(left,right,fruits)) #prints the returned value 
# print(fruits) #Since lists are mutable so it modifies the original array in place 

