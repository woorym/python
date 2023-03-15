n = int(input())

arr = list(map(int, input().split()))

check = sorted(list(set(arr)))

dic = {check[i] : i for i in range(len(check))}
for i in arr:
    print(dic[i], end = ' ')