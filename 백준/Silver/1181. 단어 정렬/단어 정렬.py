n = int(input())

arr =[]

for i in range(n):
    string = input()
    arr.append(string)

arr = list(set(arr))
arr.sort(key = lambda x : (len(x), x))

for i in arr:
    print(i)