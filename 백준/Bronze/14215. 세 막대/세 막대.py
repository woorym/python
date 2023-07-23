arr = list(map(int, input().split()))

check = max(arr)

arr.remove(check)

total = 0

for i in arr:
    total += i

while True:
    if total > check:
        break
    check -= 1

print(total + check)