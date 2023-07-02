arr = []
sum= 0

for i in range(5):
    num = int(input())
    arr.append(num)
    sum += num

mean = sum // 5
arr.sort()

print(mean)
print(arr[2])
