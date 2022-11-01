count = int(input())

for i in range(count):
    ary = list(input().split())
    for j in range(len(ary[1])):
        print(int(ary[0])*ary[1][j], end='')
    print('')
    