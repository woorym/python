import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

arr.sort(reverse=True)

sum = 0
for i in range(n):
    for j in range(i, n):
        sum += arr[j]
print(sum)