n = int(input())

arr1 = list(map(int, input().split()))

m = int(input())

arr2 = list(map(int, input().split()))

check_dict = {}

for i in arr1:
    if i in check_dict:
        check_dict[i] += 1
    else:
        check_dict[i] = 1

for i in arr2:
    if i in check_dict:
        print(check_dict[i], end=' ')
    else:
        print(0, end=' ')