import sys

input = sys.stdin.readline

def gcd(x, y):
    start = 1
    arr = []
    while start <= min(x, y):
        if x % start == 0 and y % start == 0:

            arr.append(start)

        start += 1

    arr.sort() 

    return arr[-1]


a, b = map(int, input().split())

check = gcd(a, b)

result = check * (a // check) * (b // check)

print(result)