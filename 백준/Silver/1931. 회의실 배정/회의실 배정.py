import sys

input = sys.stdin.readline

n = int(input())

# conf_time_dict = {}
conf_time = []
for _ in range(n):
    start, end = map(int, input().split())
    conf_time.append([start, end])

conf_time.sort(key=lambda x : x[0])
conf_time.sort(key=lambda x : x[1])

# print(conf_time)

# for start, end in conf_time:
    # conf_time_dict[(start, end)] = 0

num = conf_time[0][1]
cnt = 1
for i in range(1, n):
    if num <= conf_time[i][0]:
        cnt += 1
        num = conf_time[i][1] 
print(cnt)
# print(conf_time_dict)

# print(conf_time_dict)
# print(conf_time)

# cnt = 0
# for key, value in conf_time_dict.items():

# result = []
# for i in range(n - 1):
    # cnt = 1
    # start = conf_time[i]
    # check = start[0]
    # for j in range(i + 1, n):
        # end = conf_time[j]
        # print(start, end)
        # if start[1] <= end[0]:
            # cnt += 1
            # start = end
    # result.append([check, cnt])

# print(result)
# result_num = -sys.maxsize
# for num in result:
    # result_num = max(result_num, num[1])

# print(result_num)
      