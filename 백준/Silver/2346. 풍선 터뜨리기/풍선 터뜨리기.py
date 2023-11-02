from collections import deque

answer_list = []
n = int(input())
num = list(map(int, input().split()))

num_dict = {}
for element in range(1, n + 1):
    num_dict[element] = num[element - 1]

num_list = [i for i in range(1, n + 1)]
dq = deque(num_list)

point = 0
for _ in range(n):
    move = dq[point]
    i = num_dict[move]
    answer_list.append(move)

    del dq[point]
    # print(dq)
    try:
        if i > 0:
            for _ in range(i - 1):
                dq.append(dq.popleft())
        else:
            for _ in range(abs(i)):
                dq.appendleft(dq.pop())
    except:
        continue
    

for k in answer_list:
    print(k, end = " ")
# print(answer_list)