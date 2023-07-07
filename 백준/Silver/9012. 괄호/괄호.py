import sys

input = sys.stdin.readline

n = int(input())

for _ in range(n):
    check = 0
    stack = []
    data = list(input())

    for i in data:

        if i == '(':
            stack.append(i)
    
        elif i == ')':
            if len(stack) == 0:
                check = 1
                break
            stack.pop()

    if check == 0 and len(stack) == 0:
        print("YES")

    else:
        print("NO")
        
