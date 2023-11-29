# 백준 9461번
import sys

input = sys.stdin.readline

# 1 1 1 2 2 3 4 5 7 9 12 16
#홀수 1 1 2 4 7 12 21
#짝수 1 2 3 5 9 16 
# dp = [1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
dp = [0, 1, 1, 1]
n = int(input())

for i in range(101):
    # if len(dp) % 2 == 0:
        # 4  1 2
        # num = len(dp)
        # dp.append(dp[num - 3] + dp[num - 2])
    # else:
        # 3 -
        # num = len(dp)
        # dp.append(dp[num - 3] + dp[num - 2])
    num = len(dp)
    dp.append(dp[num - 3] + dp[num - 2])

for i in range(n):
    idx = int(input())
    print(dp[idx])
