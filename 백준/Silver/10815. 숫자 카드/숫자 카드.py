n = int(input())

dict1 = {}

arr1 = list(map(int, input().split()))

for i in arr1:
    dict1[i] = 0

dict2 = {}
m = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    dict2[i] = 0

for i in arr1:
    if i in dict2:
        dict2[i] += 1
# print(dict2)

for i in dict2.values():
    print(i, end = " ")