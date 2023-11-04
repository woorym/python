import sys

input = sys.stdin.readline

cnt = 1
n, m, r = list(map(int, input().split()))
line_info = [
    []
    for _ in range(n + 1)
]

for _ in range(m):
    info = list(map(int, input().split()))
    line_info[info[0]].append(info[1])
    line_info[info[1]].append(info[0])

# line_info.sort(key=lambda x : (x[0], x[1]))
for i in range(n + 1):
    line_info[i].sort()

# print(line_info)
# print(line_info)
# def bfs()
visited = [0] * (n + 1)
# print(visited)

def bfs(r):
    global cnt
    result = []
    queue = []
    visited[r] = cnt

    # result.append(r)
    queue.append(r)

    while len(queue) != 0:
        check = queue[0]
        result.append(check)
        
        del queue[0]
        # print(queue)


        for el2 in line_info[check]:
            if visited[el2] == 0:
                cnt += 1
                visited[el2] = cnt
                queue.append(el2)

    # print(0) 
    return result

result = bfs(r)
# print(visited)

for i in range(1, n + 1):
    print(visited[i])

# if len(result) == 1:
    # print(0)
# elif len(result) == n:
    # for i in result:
        # print(i)
# else:
    # for i in result:
        # print(i)
    # print(0)
# 
# for el1, el2 in line_info:
        # if el1 == 1 and visited[el2] == 0:
            # visited[el2] = 1
            # queue.append(el1)
# print(visited)
# result = bfs(1)

# print(result)

