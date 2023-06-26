n = int(input())

for i in range(n):
    num = int(input())
    a, b, c, d = 0, 0, 0, 0

    while num != 0:
        
        if num >= 25:
            a = num // 25 
            num -= 25 * a 

        elif num >= 10:
            b = num // 10
            num -= 10 * b

        elif num >= 5:
            c = num // 5
            num -= 5 * c 

        elif num >= 1:
            d = num // 1
            num -= 1 * d

    print(a, b, c, d) 