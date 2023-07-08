import sys

input = sys.stdin.readline

arr = []
stack = []
result = []

check = 0 

n = int(input())

for _ in range(n):
    arr.append(int(input()))



for i in range(1, n + 1):
    

    stack.append(i)
    result.append("+")

    while stack[-1] == arr[check]:
        stack.pop()
        result.append("-")
        check += 1

        if stack == []:
            break

        if check == len(arr):
            break

    
if len(result) == 2 * n:
    for i in result:
        print(i)

else:
    print("NO")



