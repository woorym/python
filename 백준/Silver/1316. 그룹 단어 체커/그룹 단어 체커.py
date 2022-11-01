num= int(input())

name=[]
result=[]

for k in range(num):
    name.append(input())

for t in range(len(name)):
    count1=0
    sum=0
    
    ary = sorted(set(name[t]))
    
    for i in range(len(ary)):
        k= name[t].find(ary[i])
        p = name[t].count(ary[i])

        for j in range(k+p,len(name[t])):
            if name[t][j] == ary[i]:
                count1+=1
    if count1 ==0:
        result.append(t)

print(len(result))