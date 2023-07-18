import sys

input = sys.stdin.readline

tmp = int(input())

total = 0
arr = []

for _ in range(tmp):
    cmd = input()

    if cmd == "ENTER\n":
        total += len(set(arr))
        arr = []
        continue
    arr.append(cmd)

total += len(set(arr))

print(total)