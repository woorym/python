n, m = list(map(int, input().split()))

arr = [0] * n

for _ in range(m):
    i, j, k = list(map(int, input().split()))

    for t in range(i - 1, j):
        arr[t] = k

for i in arr:
    print(f"{i} " , end = "")