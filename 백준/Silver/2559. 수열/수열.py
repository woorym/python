import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))

arr = list(map(int, input().split()))

check = []
check.append(sum(arr[:k]))

for i in range(n - k):
    check.append(check[i] - arr[i] + arr[k + i])

print(max(check))
