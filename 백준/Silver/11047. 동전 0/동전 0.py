import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num_list = []
sum_cnt = 0

for _ in range(n):
    num_list.append(int(input()))

charge = k
for num in reversed(num_list):
    cnt = 0
    if charge >= num:
        cnt += charge // num
        charge -= num * cnt
        sum_cnt += cnt
        
    else:
        continue

print(sum_cnt)