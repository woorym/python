num = int(input())
result = 0
k=0
i=0

while num!=1:

    i+=1

    range = (i*(i+1))/2
    
    range1 = ((i+1)*(i+2))/2

    if num>range and num<=range1:
        result = i+1
        break
    

if num==1:
    print('1/1')

# print(f'result : {result}')


result1 =((result-1)*result) //2
check = 0
#result1 는 앞 개수
# print(f'result1 : {result1}')
while num!=1:
    
    num1=1
    num2=0
    while result%2==0:
        
        if num==result1+1:
            print(f'{num1}/{result-num2}')
            check=1
            break
        num1+=1
        num2+=1
        result1+=1



    while result%2==1:
        if num==result1+1:
            print(f'{result-num2}/{num1}')
            check=1
            break
        num1+=1
        num2+=1
        result1+=1
    if check==1:
        break


