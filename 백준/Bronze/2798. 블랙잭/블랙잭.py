import sys

input = sys.stdin.readline

n, m = list(map(int, input().split()))

num_list = list(map(int, input().split()))

arr = []
sum = 0

for i in range(0, len(num_list) - 2):
    for j in range(i + 1, len(num_list) - 1):
        for k in range(j + 1, len(num_list)):
            sum = num_list[i] + num_list[j] + num_list[k]

            if sum <= m:
                arr.append(sum)

arr.sort(reverse=True)

print(arr[0])