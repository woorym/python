n, m = list(map(int, input().split()))
    
def fac(n):
    sum = 1
    
    for i in range(1, n + 1):
        sum *= i
       
    return sum

result = fac(n) / (fac(m) * fac(n - m))
            
print(int(result))
        