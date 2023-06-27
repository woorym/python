arr_x = [] 
arr_y = [] 

for _ in range(3):
    a, b = list(map(int, input().split()))
        
    arr_x.append(a)
    arr_y.append(b)

for i in range(3):
    if arr_x.count(arr_x[i]) == 1:
        a = arr_x[i]

    if arr_y.count(arr_y[i]) == 1:
        b = arr_y[i]

print(a, b)