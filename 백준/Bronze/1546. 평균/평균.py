num = int(input())
sum =0
ary = list(map(int, input().split()))
result = ary[0]

for i in range(len(ary)-1):
    
    if result<ary[i+1]:
        result = ary[i+1]

# print(result)

for i in range(len(ary)):
    
    # if not result ==ary[i]:
    sum += (ary[i]/result)*100

    # else:
    #     sum+=result

print(sum/len(ary))    