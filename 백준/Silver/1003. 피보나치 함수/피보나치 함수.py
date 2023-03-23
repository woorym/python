n = int(input())
for _ in range(n):
    num = int(input())
    zero,one=1,0 
    for i in range(num):
        zero,one = one,zero+one 
    print(zero,one)