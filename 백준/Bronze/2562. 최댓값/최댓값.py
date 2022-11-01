ary = []
count = 0

for i in range(9):
    num = int(input())
    ary.append(num)

result = ary[0]

for i in range(len(ary)-1):
    if result <ary[i+1]:
        result = ary[i+1]
for j in ary:
    if j == result:
        count+=1
        break
    count+=1
print(result)
print(count)
