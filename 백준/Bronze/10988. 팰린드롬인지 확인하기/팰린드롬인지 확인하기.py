test = input()
check = test

arr1 = list(check)
arr2 = list(test)
arr2.reverse()

check = 0

for i, j in enumerate(arr1):
    if j != arr2[i]:
        print(0)
        break
    check += 1

if check == len(arr1):
    print(1)
