num = int(input())

for i in range(num):

    sum=0
    count=0
    
    ary = list(map(int, input().split()))

    for j in range(1,len(ary)):
        sum+=ary[j]

    for k in range(1,len(ary)):

        if ary[k]>sum/(len(ary)-1):
            count+=1
    print('%.3f%%' %(count/(len(ary)-1)*100))