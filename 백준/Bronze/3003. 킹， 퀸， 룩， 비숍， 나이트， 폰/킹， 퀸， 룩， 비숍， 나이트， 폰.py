a,b,c,d,e,f = map(int, input().split())

list=[1,1,2,2,2,8]

list1=[a,b,c,d,e,f]

for i in range(len(list)):
    if list1[i]!=list[i]:
        list[i]-=list1[i]
    else:
        list[i]=0

for i in range(len(list)):
    print(list[i], end= ' ')