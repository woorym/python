import sys

list = []
n = int(sys.stdin.readline())

for i in range(n):

    a = int(sys.stdin.readline())

    list.append(a)

list = sorted(list)

for i in list:
    print(i)    