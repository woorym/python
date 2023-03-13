a, b = list(map(int, input().split()))
arr = []
for i in range(1, a + 1):
    arr.append(i)
for _ in range(b):
    i, j = list(map(int, input().split()))
    i -= 1
    j -= 1
    take = arr[i]
    arr[i] = arr[j]
    arr[j] = take

for i in arr:
    print(f"{i} ", end = "")