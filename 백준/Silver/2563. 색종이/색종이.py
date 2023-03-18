arr = [
    [0] * 100
    for _ in range(100)
]

num = int(input())

for _ in range(num):

    n, m = list(map(int, input().split()))
    for i in range(n, n + 10):
        for j in range(90 - m, 100 - m):
            arr[i][j] = 1


count = 0

for i in range(100):
    for j in range(100):
        if arr[i][j] == 1:
            count += 1

print(count)