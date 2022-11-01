num = int(input())

ary = list(map(int, input().split()))
result = ary[0]
result1 = ary[0]
for i in range(len(ary)-1):
    if result <ary[i+1]:
        result = ary[i+1]
    elif result1>ary[i+1]:
        result1 = ary[i+1]

print(result1,result)
