ary1 = []

while True:
    x,y = map(int, input().split())

    
    if x==0 and y==0:
        break    
    ary1.append(x+y)

for i in range(len(ary1)):
    print(ary1[i])