def num(a):
    new = str(a)
    sum = 0
    for i in range(len(new)):
        sum +=int(new[i])

    result = sum+a

    return result

ary = []
ary1 = []
for i in range(10000):
    ary.append(num(i))

for i in range(10000):
    ary1.append(i)

total = list(set(ary1)-set(ary))


for i in sorted(total):
    print(i)
