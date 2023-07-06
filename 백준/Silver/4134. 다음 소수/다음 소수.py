import sys

input = sys.stdin.readline

arr = []
case = int(input())

for _ in range(case):
    
    test = int(input())
    if test <= 1:
        print(2)
        continue
    prim_num = test
    while True:
        count = 0
        for j in range(2, int(prim_num ** 0.5) + 1):
            if prim_num % j == 0:
                count += 1
                break
        if count == 0:
            break
        prim_num += 1
        
    print(prim_num) 
