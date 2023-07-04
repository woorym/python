import sys

input = sys.stdin.readline

n = int(input())

arr = []
for _ in range(n):
    name, check = list(map(str, input().split()))

    if check == "enter":
        arr.append(name)
    
    elif check == "leave":
        arr.remove(name)

arr.sort(reverse=True)

for i in arr:
    print(i)