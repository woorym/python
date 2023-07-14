import sys

input = sys.stdin.readline

def gdp(x, y):
    count = 1
    check_list = []
    while count <= min(x, y):
        if x % count == 0 and y % count == 0:
            check_list.append(count)
        
        count += 1 

    return check_list[-1]

test_case = int(input())

for _ in range(test_case):
    x, y = list(map(int, input().split()))
    num = gdp(x, y)

    result = num * (x // num) * (y // num)

    print(result)

            