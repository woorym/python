# 백준 7562번
from collections import deque
import sys
input = sys.stdin.readline

# 킹이 움직일 수 있는 곳들
dxs = [-2, -1, 1, 2, 2, 1, -1, -2]
dys = [1, 2, 2, 1, -1, -2, -2, -1]

test_case = int(input())

for _ in range(test_case):
    map_size = int(input())

    # 체스판의 크기
    graph = [
        [0] * map_size
        for _ in range(map_size)
    ]

    #방문했는지 확인
    visited = [
        [False] * map_size
        for _ in range(map_size)
    ]

    # 나이트의 현재 위치와 최종 목적지
    knight_cur_x, knight_cur_y = map(int, input().split()) 
    knight_dt_x, knight_dt_y = map(int, input().split())

    #체스판 안에서 움직이게 하기
    def in_range(x, y):
        return x >= 0 and x < map_size and y >= 0 and y < map_size

    def bfs():
        queue = deque()
        queue.append([knight_cur_x, knight_cur_y])
        graph[knight_cur_x][knight_cur_y] = 0
        visited[knight_cur_x][knight_cur_y] = True
        
        while queue:
            nx, ny = queue.popleft()
            for dx, dy in zip(dxs, dys):
                mv_x, mv_y = nx + dx, ny + dy

                if in_range(mv_x, mv_y) and not visited[mv_x][mv_y]:
                    if not (mv_x == knight_dt_x and mv_y == knight_dt_y):
                        visited[mv_x][mv_y] = True
                        graph[mv_x][mv_y] = graph[nx][ny] + 1
                        queue.append([mv_x, mv_y])
                    else:
                        graph[mv_x][mv_y] = graph[nx][ny] + 1
                        return
                    
    bfs()

    # for i in range(map_size):
        # for j in range(map_size):
            # print(graph[i][j], end = " ")
        # print()

    print(graph[knight_dt_x][knight_dt_y])