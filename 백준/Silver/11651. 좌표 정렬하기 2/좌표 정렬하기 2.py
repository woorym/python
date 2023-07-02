n = int(input())
arr = []

for _ in range(n):
    pos = list(map(int, input().split()))
    arr.append(pos)

arr.sort(key = lambda x : (x[1], x[0]))

for i, j in arr:
    print(i, j)