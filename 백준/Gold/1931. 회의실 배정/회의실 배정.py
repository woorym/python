import sys
input = sys.stdin.readline

n = int(input())
time_list = []

for i in range(n):
    start, end = map(int, input().split())
    time_list.append([start, end])


time_list.sort(key=lambda x: x[0])
time_list.sort(key=lambda x: x[1])

num = time_list[0][1]
cnt = 1
for i in range(1, n):
    if num <= time_list[i][0]:
        cnt += 1
        num = time_list[i][1]
print(cnt)