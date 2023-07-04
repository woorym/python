import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))

arr = {}
count = 1 

for _ in range(n):
    name = input()[:-1]
    arr[name] = count
    count += 1

check = {v : k for k, v in arr.items()}

for _ in range(m):
    try:
        test = input()[:-1]
        print(check[int(test)])
    except:
        print(arr[test])