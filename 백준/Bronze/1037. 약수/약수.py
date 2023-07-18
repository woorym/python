import sys

input = sys.stdin.readline

test_case = int(input())

arr = list(map(int, input().split()))

arr.sort()

real_num = arr[0] * arr[-1]

print(real_num)