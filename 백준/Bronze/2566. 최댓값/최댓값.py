import sys

arr = [
    list(map(int, input().split()))
    for _ in range(9)
]

max = -sys.maxsize

for i in range(9):
    for j in range(9):
        if max < arr[i][j]:
            max = arr[i][j]
            check_x = i + 1
            check_y = j + 1
print(max)
print(check_x, check_y)