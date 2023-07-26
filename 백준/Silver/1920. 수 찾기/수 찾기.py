n = int(input())

arr1 = list(map(int, input().split()))

arr1_dict = {i : 0 for i in arr1}

m = int(input())

arr2 = list(map(int, input().split()))

for i in arr2:
    if i in arr1_dict:
        print(1)
    else:
        print(0)
    