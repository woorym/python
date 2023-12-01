# 백준 1912번
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], dp[i - 1] + arr[i])
    # check = []
    # check.append(dp[i] + dp[i + 1])
    # for j in range(i + 1, n - 1):
        # check.append(check[-1] + dp[j + 1])
    # print(j)
    # if j == n - 2:
        # check = check[:-1]
    # print(check)
    # dp.append(max(check))
# print(max(dp))
# print(len(dp))
# print(dp)
print(max(dp))