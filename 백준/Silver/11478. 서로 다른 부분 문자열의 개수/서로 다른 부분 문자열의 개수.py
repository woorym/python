str = input()

count = 1
arr = []
len = len(str)

while True:
    for i in range(len + 1):
        if i + count > len:
            continue
        add = str[i : i + count]
        arr.append(add)
    

    if len == count:
        break
    count += 1


arr = set(arr)

sum = 0
for i in arr:
    sum += 1
print(sum)