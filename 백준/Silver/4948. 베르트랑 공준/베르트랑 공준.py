ary = []

for i in range(2,246913):
  count = 0
    
  for j in range(2,int(i**0.5)+1):
      
    if i%j==0:
        count+=1
        break
  if count ==0:
    ary.append(i)


while True:
  n = int(input())

  res = 0

  if n==0:
    break
  
  for i in ary:
    if n<i<=2*n:
      res+=1
  print(res)