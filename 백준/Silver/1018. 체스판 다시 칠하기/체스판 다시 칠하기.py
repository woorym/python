# 백준 1018번
import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

result = [
    list(input().rstrip())
    for _ in range(n)
]

check1 = [[] for _ in range(n)]
check2 = [[] for _ in range(n)]

flag1 = 0
for i in range(8):
    for j in range(8):
        if flag1 == 0:
            check1[i].append("B")
            check2[i].append("W")
            flag1 = 1
        else:
            check1[i].append("W")
            check2[i].append("B")
            flag1 = 0
    if i % 2 == 0:
        flag1 = 1
    else:
        flag1 = 0

# sum1, sum2 = 0, 0
check_a, check_b = 0, 0
result_list = []
for a in range(n - 8 + 1):
    check_a = a
    for b in range(m - 8 + 1):
        sum1, sum2 = 0, 0
        check_b = b
        for i in range(8):
            for j in range(8):
                if result[i + check_a][j + check_b] != check1[i][j]:
                    sum1 += 1
                if result[i + check_a][j + check_b] != check2[i][j]:
                    sum2 += 1
        result_list.append(sum1)
        result_list.append(sum2)


print(min(result_list))
# print(min(sum1, sum2))
# print(sum1)
# print(sum2)