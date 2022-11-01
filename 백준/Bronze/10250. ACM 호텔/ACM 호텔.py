test = int(input())
ary = []

for i in range(test):
    ary.append(input().split())

for i in range(len(ary)):

    h = int(ary[i][0])
    w = int(ary[i][1])
    n = int(ary[i][2])
    y = n/h 
    x = n%h 
    if y -(n//h)>0:
        y+=1

    if y<10:
        if x!=0:
            print("%d" %(x*100+y))
        else:
            print("%d" %(h*100+y))
    else:
        if x!=0:
            print("%d" %(x*100+y))
        else:
            print("%d" %(h*100+y))   