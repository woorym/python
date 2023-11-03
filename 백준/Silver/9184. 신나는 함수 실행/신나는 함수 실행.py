import  sys

input = sys.stdin.readline


# global i
dp = [[[0] * 21 for _ in range(21)] for _ in range(21)]

def first(a, b, c):
    # i = 0
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        # i += 1
        # print(f"i : {i}")
        return first(20, 20, 20)
    
    if dp[a][b][c]:
        return dp[a][b][c]
    
    if a < b and b < c:
        # print(f"i : {i}")
        # num = first(a, b, c - 1) + first(a, b - 1, c - 1) - first(a, b - 1, c)
        # return num
        dp[a][b][c] = first(a, b, c - 1) + first(a, b - 1, c - 1) - first(a, b - 1, c) 
        return dp[a][b][c]

    num1 = first(a - 1, b, c)
    num2 = first(a - 1, b - 1, c)
    num3 = first(a - 1, b, c - 1)
    num4 = first(a - 1, b - 1, c - 1)

    dp[a][b][c] = num1 + num2 + num3 - num4
    return dp[a][b][c]

# first(1, 2, 3)
while True:
    a, b, c = list(map(int, input().split()))

    if a == -1 and b == -1 and c == -1:
        break

    result = first(a, b, c)
    print(f"w({a}, {b}, {c}) = {result}")