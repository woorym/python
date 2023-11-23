import sys

input = sys.stdin.readline

# 0 0 1 1
arr = [0] * 1000001
arr[2], arr[3] = 1, 1

for i in range(4, 1000001):
    cnt = 1
    check1 = check2 = check3 = sys.maxsize
    if i % 3 == 0:
        check1 = arr[i // 3] + cnt
    if i % 2 == 0:
        check2 = arr[i // 2] + cnt
        # if i - 1 == 1:
    check3 = arr[i - 1] + cnt
        # else:
            # continue
    win1 = min(check1, check2)
    arr[i] = min(win1, check3)
# print(arr[11])
n = int(input())
print(arr[n])

# 10 -> 9 -> 3 -> 1
# 1000000