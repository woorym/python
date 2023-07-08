import sys

input = sys.stdin.readline

num = int(input())
new_arr = []

for i in range(1000000):
    sum = 0
    arr = list(str(i))
    
    sum += i

    for j in arr:
        sum += int(j)
    
    

    if sum == num:
        new_arr.append(i)
        break
    

new_arr.sort()
if new_arr == []:
    print(0)
else:
    print(new_arr[0])
