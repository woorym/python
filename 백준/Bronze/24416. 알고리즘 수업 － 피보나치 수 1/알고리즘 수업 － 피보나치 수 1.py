import sys
input = sys.stdin.readline

cnt1, cnt2 = 0, 0
def fib(n):
    global cnt1
    cnt1 += 1
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

arr = [1, 1]
def fibonacci(n):
    global cnt2
    for _ in range(2, n):
        arr.append(arr[-1] + arr[-2])
        cnt2 += 1
    return arr

n = int(input())
fibonacci(n)

print(fib(n), cnt2)
# print(arr)
# print(fib(2))
    
    