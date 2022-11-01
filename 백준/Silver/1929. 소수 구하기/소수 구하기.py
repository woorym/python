ary =[]

n,m = map(int, input().split())

for i in range(2,1000000):
  count = 0
  for j in range(2,int(i**0.5)+1):
    if i%j==0:
      count+=1
      break
  if count ==0:
    ary.append(i)

for i in ary:
  if n<=i<=m:
    print(i)