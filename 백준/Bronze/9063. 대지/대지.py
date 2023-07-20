n = int(input())
x_set = set()
y_set = set()

if n == 1:
    print(0)
    
else:
    for i in range(n):
        x, y = map(int, input().split())
        x_set.add(x)
        y_set.add(y)

    print((max(x_set) - min(x_set)) * (max(y_set) - min(y_set)))