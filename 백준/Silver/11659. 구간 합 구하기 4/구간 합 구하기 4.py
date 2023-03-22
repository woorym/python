import sys

n, m = list(map(int, sys.stdin.readline().split()))
# print(n)

arr = list(map(int, sys.stdin.readline().split()))
total = 0
total1 = [0]
for i in arr:
    total += i
    total1.append(total)



for _ in range(m):
    i, j = list(map(int, sys.stdin.readline().split()))

    result = total1[j] - total1[i - 1]

    sys.stdout.write(str(result) + "\n")


