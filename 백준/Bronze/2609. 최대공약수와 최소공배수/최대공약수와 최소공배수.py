a, b = map(int, input().split())
i = 1

while True:

    if a % i == 0 and b % i ==0:
        answer1 = i
        
    elif i > a and i > b:
        break
    
    i += 1

answer2 = int(a * b / answer1)

print(answer1)
print(answer2)