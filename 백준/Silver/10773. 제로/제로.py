ary = []
sum = 0
num = int(input())

for i in range(num):

    number = int(input())

    if number == 0:
        ary.pop()
    else:
        ary.append(number)


for i in ary:
    sum += i

print(sum)