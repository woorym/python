n, k = list(map(int, input().split()))

check = 0

for i in range(1, n + 1):
    if n % i == 0:
        check += 1
    
    if check == k:
        print(i)
        break

if check < k:

    print(0)