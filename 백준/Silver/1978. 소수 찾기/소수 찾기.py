num = int(input())

ary = list(map(int,input().split()))
sum = 0
for i in range(num):
    count = 0
    for j in range(1,ary[i]+1):

        if ary[i]%j==0:
            count+=1
    if count ==2:
        sum+=1

print(sum)