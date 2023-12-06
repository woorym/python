# 백준 1436번
import sys
input = sys.stdin.readline

n = int(input())

cnt = 1
num = 665
while cnt <= n:
    start = list(str(num))
    # print(start)

    for i in range(len(start) - 2):
        if start[i] == '6':
            if start[i + 1] == '6':
                if start[i + 2] == '6':
                    cnt += 1
                    break
    result = num
    num += 1

print(result)
    