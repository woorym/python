n,x = map(int, input().split())

list1 = []

ary = list(map(int, input().split()))

for i in range(len(ary)):
    if ary[i]<x:
        list1.append(ary[i])

for i in range(len(list1)):
    print(list1[i], end = ' ')