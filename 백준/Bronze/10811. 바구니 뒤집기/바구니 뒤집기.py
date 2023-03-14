n, m = map(int, input().split())

data = [i for i in range(n + 1)]

for _ in range(m) :
  i, j = map(int, input().split())
  arr = []
  for k in range(i, j + 1) :
    arr.append(data[k])
  
  arr = arr[::-1]
  number = 0
  for k in range(i, j + 1) :
    data[k] = arr[number]
    number += 1

for k in range(1, len(data)) :
  print(data[k], end=' ')