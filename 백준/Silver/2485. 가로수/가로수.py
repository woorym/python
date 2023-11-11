import sys
from math import gcd

input = sys.stdin.readline

n = int(input())

a = int(input())

arr = []
for _ in range(n - 1):
    num = int(input())
    arr.append(num - a)
    a = num

# print(arr)

g = arr[0]
for j in range(1, len(arr)):
    g = gcd(g, arr[j])

result = 0
for element in arr:
    result += element // g - 1

print(result)