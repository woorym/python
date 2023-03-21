import sys

N, L = map(int, sys.stdin.readline().split())

for i in range(L, 101):
    x = N - (i * (i + 1) / 2)
    temp = ""

    if x % i == 0:
        x = int(x / i)

        if x >= -1:
            for j in range(1, i + 1):
                temp += f"{x + j} "
            print(temp)
            break
else:
    print(-1)