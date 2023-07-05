n, m = list(map(int, input().split()))

arr = {} 

for _ in range(n):
    name = input()

    if name in arr:
        arr[name] += 1
    elif len(name) >= m:
        arr[name] = 1

arr = sorted(arr.items())
arr.sort(key = lambda x : (-x[1], -len(x[0]), x[0] ))

for element in arr:
    print(element[0])