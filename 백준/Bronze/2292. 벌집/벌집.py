num = int(input())

a=1
t=0
result = 1
while True:
    
    num1=a
    t+=1
    a+=6*t

    if num==1:
        break

    elif num>num1 and num<=a:    
        result = t+1
        break

print(result)
