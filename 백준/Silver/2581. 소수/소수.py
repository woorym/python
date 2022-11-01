num1 = int(input())
num2 = int(input())
ary = []

sum = 0
for i in range(num1,num2+1):
    count = 0
    for j in range(1,i+1):

        if i%j==0:
            count+=1
    if count ==2:
        ary.append(i)        

for i in range(len(ary)):
    
    sum+=ary[i]

if sum!=0:
    print(sum)
    print(ary[0])
else:
    print(-1)