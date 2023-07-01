n = int(input())

arr = []

for _ in range(n):
    age, name = list(input().split())
    arr.append((int(age), name))
    

# arr.sort(key = lambda x : (x[0], reverse_string(x[1])))
arr.sort(key = lambda x : x[0])
# arr.sort(key = lambda x : x[1], reverse = True)


# print(arr[0])
for i, j in arr:
    print(i, j)