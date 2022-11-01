total = int(input())
count = int(input())

ary = []
sum = 0
for i in range(count):
    ary.append(list(map(int,input().split())))

for a,b in ary:
    result = a*b
    sum+=result

if total ==sum:
    print('Yes')
else:
    print('No')