num = int(input())
real =-8
count=0

fake = num

while not num==real:

    if fake>=10:
        new = (fake//10 + fake%10)%10
        real = (fake%10)*10+new
        count+=1


    elif fake<10:
        real = fake*10+fake
        count+=1

    fake = real
    
    

print(count)