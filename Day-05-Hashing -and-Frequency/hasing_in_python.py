n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

freq_map ={}

for num in n:
  if num in freq_map:
    freq_map[num] += 1
  else:
    freq_map[num] = 1

print(freq_map)

for num in m:
  if num in freq_map:
    print(freq_map[num])
  else:
    print(0)


#USING HASH LIST IS THERE IN NOTES