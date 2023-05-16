n, m = list(map(int, input().split()))

arr = [i for i in range(1, n + 1)]

for _ in range(m):
    i, j , k = list(map(int, input().split()))
    arr = arr[:i - 1] + arr[k - 1:j] + arr[i - 1:k - 1] + arr[j:]

for i in arr:
    print(i, end = " ")