#체스판
chess_map = [
            [0] * 8
            for _ in range(8)
            ]

#밖으로 나갈경우 함수
def is_in(x, y):
    return x >= 0 and x < 8 and y >= 0 and y < 8

#딕셔너리
pos_dict = {'A' : 0, 'B' : 1, 'C' : 2, 'D' : 3, 'E' : 4, 'F' : 5, 'G' : 6, 'H' : 7}

king_pos, ball_pos, num = list(map(str, input().split()))
#열 행
king_pos_list, ball_pos_list = list(king_pos), list(ball_pos)

#킹의 위치
nx1, ny1 = 8 - int(king_pos_list[1]), pos_dict[king_pos_list[0]]

#볼의 위치
nx2, ny2 = 8 - int(ball_pos_list[1]), pos_dict[ball_pos_list[0]]


num = int(num)
for _ in range(num):

    #조건
    request = input()
    #x는 행, y는 열
    x, y = 0, 0

    #한 칸 오른쪽
    if request == 'R':
        x, y = 0, 1
        
    #한 칸 왼쪽
    elif request == 'L':
        x, y = 0, -1

    #한 칸 아래로
    elif request == 'B':
        x, y = 1, 0
        
    #한 칸 위로
    elif request == 'T':
        x, y = -1, 0

    #오른쪽 위 대각선으로
    elif request == 'RT':
        x, y = -1, 1

    #왼쪽 위 대각선으로
    elif request == 'LT':
        x, y = -1, -1

    #오른쪽 아래 대각선으로
    elif request == 'RB':
        x, y = 1, 1

    #왼쪽 아래 대각선으로
    elif request == 'LB':
        x, y = 1, -1

    #둘 다 이동 가능 할 때
    if(is_in(nx1 + x, ny1 + y) and is_in(nx2 + x, ny2 + y)):
        chess_map[nx1][ny1] = 0
        chess_map[nx2][ny2] = 0
        #킹의 위치
        if(nx1 + x == nx2 and ny1 + y == ny2):
            nx1, ny1 = nx1 + x, ny1 + y
            nx2, ny2 = nx2 + x, ny2 + y
        else:
            nx1, ny1 = nx1 + x, ny1 + y
    # 킹은 못움직이고, 볼만 움직일 수 있을 때
    elif(not is_in(nx1 + x, ny1 + y) and is_in(nx2 + x, ny2 + y)):
        pass
        
    #킹은 움직이고, 볼만 못움직일 때
    elif(is_in(nx1 + x, ny1 + y) and not is_in(nx2 + x, ny2 + y)):
        if(nx1 + x == nx2 and ny1 + y == ny2):
            pass
        else:
            nx1, ny1 = nx1 + x, ny1 + y
            
    chess_map[nx1][ny1] = 1
    chess_map[nx2][ny2] = 2

# for arr in chess_map:
    # print(arr)


result_dict = {0 : 'A', 1 : 'B', 2 : 'C', 3 : 'D', 4 : 'E', 5 : 'F', 6 : 'G', 7 : 'H'}

print(f"{result_dict[ny1]}{8 - nx1}")
print(f"{result_dict[ny2]}{8 - nx2}")
