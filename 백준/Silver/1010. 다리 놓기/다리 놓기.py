def fac(num):
    sum = 1
    for i in range(1,num+1):
        sum *= i
    return sum

test_case = int(input())

for i in range(test_case):

    a, b = map(int, input().split())

    result = fac(b)/(fac(a)*fac(b-a))

    print(int(result))

