num = int(input())

for i in range(num):
    test = list(input())

    score=0
    sum=0

    for j in range(len(test)):
        

        if test[j]=='O':

            score+=1
        else:
            score =0

        sum+=score    

    print(sum)
