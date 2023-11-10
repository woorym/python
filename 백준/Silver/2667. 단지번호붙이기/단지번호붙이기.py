from collections import deque
import sys

input = sys.stdin.readline

cnt = 0

n = int(input())

graph = [
    list(input())[:-1]
    for _ in range(n)
]

visited = [
    [0] * n
    for _ in range(n)
]
#     동 남 서 북
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

def in_range(x, y):
    return x >= 0 and x < n and y >= 0 and y < n

def bfs():
    global cnt
    queue = deque()

    
    for i in range(n):
        for j in range(n):
            start_x, start_y = i, j
            if graph[start_x][start_y] == '1' and visited[start_x][start_y] == 0:
                queue.append([start_x, start_y])            
                cnt += 1 

            while queue:
                nx, ny = queue.popleft()
                visited[nx][ny] = cnt
                list = []
                for kx, ky in zip(dxs, dys):
                    test_x, test_y = nx, ny

                    test_x += kx
                    test_y += ky

                    list.append([test_x, test_y])
                
                for x1, y1 in list:
                    if in_range(x1, y1) and graph[x1][y1] == '1' and visited[x1][y1] == 0:
                        visited[x1][y1] = cnt
                        queue.append([x1, y1])
            

bfs()

result = []
for i in range(n):
    for j in range(n):
        result.append(visited[i][j])

result_dict = {}
for i in set(result):
    if i == 0:
        continue
    result_dict[i] = 0

for i in range(n):
    for j in range(n):
        num = visited[i][j]
        if num == 0:
            continue

        result_dict[num] += 1

# print(result_dict)
result_list = []
for values in result_dict.values():
    result_list.append(values)

# del result_list[0]
# print(result_list)

# print(result_list)
print(len(result_list))
for i in sorted(result_list):
    print(i)
