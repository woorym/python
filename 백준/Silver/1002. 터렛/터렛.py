test_case = int(input())

for i in range(test_case):

    x1,y1,r1,x2,y2,r2 = map(int, input().split())

    length= ((x2-x1)**2 + (y2-y1)**2)**0.5

    if x1 ==x2 and y1 == y2:
        if r1 == r2:
            print(-1)
        else:
            print(0)
    elif length > r1 + r2:
        print(0)
    elif length == r1 + r2:
        print(1)
    elif length < r1 + r2:
        if r1 > r2:
            if length > r1 - r2:
                print(2)
            elif length < r1 - r2:
                print(0)
            else:
                print(1)
        if r1 == r2:
            print(2)
        if r1 < r2:
            if length > r2 - r1:
                print(2)
            elif length < r2 - r1:
                print(0)
            else:
                print(1)