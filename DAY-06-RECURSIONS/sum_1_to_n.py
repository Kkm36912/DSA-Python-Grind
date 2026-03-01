n = int(input())
sum = 0
def func(sum,i, n):
  if n == 0:
    print(sum)
    return
  func(sum+i,i+1, n-1)
func(sum,1,n)