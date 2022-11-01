num = int(input())
list = []
check = []

a = num//5

while a!=-1:
    b = (num-a*5)/3
    if b%1 !=0:
        a-=1
        continue

    list.append(a+b)
    a-=1

if list !=check:
    first = list[0]

    for i in range(1,len(list)):
    
        if first > list[i]:
            first = list[i]

    print(int(first))

else:
    print(-1)