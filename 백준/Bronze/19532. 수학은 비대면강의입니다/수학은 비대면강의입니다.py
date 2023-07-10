# import numpy as np

# arr = list(map(int, input().split()))

# x = np.array([[arr[0], arr[1]],
#                [arr[3], arr[4]]])

# y = np.array([[arr[2]],
#               [arr[5]]])

# x = np.linalg.inv(x)

# result = np.dot(x, y)

# for i in result:
#     print(round(i[0]), end = " ")

arr = list(map(int, input().split()))

for i in range(-999, 1000):
    for j in range(-999, 1000):
        if (arr[0] * i) + (arr[1] * j) == arr[2] and (arr[3] * i) + (arr[4] * j) == arr[5]:
            print(i, j)