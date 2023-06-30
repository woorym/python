a, b = list(map(int, input().split()))

c, d = list(map(int, input().split()))

num1 = a * d + b * c
num2 = b * d


def gcd(x,y): 
    mod = x % y
    while mod >0:
        x = y
        y = mod
        mod = x % y
    return y  

result = gcd(num1, num2)


print(num1 // result, num2 // result) 