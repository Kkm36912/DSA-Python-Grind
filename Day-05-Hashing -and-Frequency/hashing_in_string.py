s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

freq_map = {}
for ch in s:
  if ch in freq_map:
    freq_map[ch] += 1
  else:
    freq_map[ch] = 1

for ch in q:
  if ch in freq_map:
    print(freq_map[ch])
  else:
    print(0)