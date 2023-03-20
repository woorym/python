import sys

arr = [True] * 1000001

arr[0] = arr[1] = False

for i in range(2, 1001):
    if arr[i]:
        for j in range(i * i, 1000001, i):
            arr[j] = False

num = int(sys.stdin.readline())

for _ in range(num):
    check_num = int(input())
    count = 0
    for j in range(2, check_num // 2 + 1):
        if arr[j] and arr[check_num - j]:
            count += 1
    sys.stdout.write(str(count) + "\n")