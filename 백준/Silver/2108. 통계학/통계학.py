import sys

n = int(sys.stdin.readline())

arr = []

#입력 된 수 배열에 넣기
for _ in range(n):
    num = int(sys.stdin.readline())
    arr.append(num)

#산술평균 구하기
total = 0
for arr_num in arr:
    total += arr_num

mean = round(total / n)
sys.stdout.write(f"{mean}\n")

#중앙값 구하기
arr.sort()
mid_num = int(n // 2)
sys.stdout.write(str(arr[mid_num]) + "\n")

#최빈값 구하기
dic = {}

for lst in arr:
    if lst not in dic:
        dic[lst] = 1
    else:
        dic[lst] += 1

max_value = max(dic.values())

max_list = [k for k, v in dic.items() if v == max_value]

if len(max_list) >= 2:
    sys.stdout.write(str(sorted(max_list)[1]) + "\n")
else:
    sys.stdout.write(str(max_list[0]) + "\n")

#범위
sys.stdout.write(str(arr[-1] - arr[0]))