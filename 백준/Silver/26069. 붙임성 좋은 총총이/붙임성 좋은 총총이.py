import sys

input = sys.stdin.readline

test_case = int(input())
arr = []

for _ in range(test_case):
    name1, name2 = input().split() 

    if name1 == "ChongChong" or name2 == "ChongChong":
        arr.append(name1)
        arr.append(name2)

    if name1 in arr:
        arr.append(name2)

    elif name2 in arr:
        arr.append(name1)
    
print(len(set(arr)))