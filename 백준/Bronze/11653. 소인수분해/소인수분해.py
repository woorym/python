num = int(input())
total =num
ary = []
count=0
while count!=2:
    count = 0
    for i in range(2,total+1):
    
        if (num/i) %1 ==0:
            ary.append(i)
            num=num/i
            break
    
    for j in range(1,int(num+1)):

        if num%j==0:
            count+=1
    if count==2:
        ary.append(int(num))
    if num==1:
        break

for i in range(len(ary)):
    print(ary[i])