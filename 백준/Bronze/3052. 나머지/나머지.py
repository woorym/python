ary = []
count = 0
for i in range(10):
    a = int(input())

    result = a%42
    ary.append(result)

for j in range(len(list(set(ary)))):
    count+=1

print(count)
