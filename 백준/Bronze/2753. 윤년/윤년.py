A =int(input())

if A %4==0:
    if not A%100==0 or A%400 ==0:
        print(1)
    else:
        print(0)        
else:
    print(0)