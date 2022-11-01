string = input()
list1=[]
list2=[]
final=[]
count = 0
check = 0
ary = list(string)

for i in range(65,91):

    list1.append(string.count(chr(i)))

for i in range(97,123):
    
    list2.append(string.count(chr(i)))

for i in range(len(list1)):
    final.append(list1[i]+list2[i])

fake = final[0]

for i in range(len(final)-1):

    if fake<final[i+1]:
        fake = final[i+1]
    

for i in range(len(final)):
    if fake == final[i]:
        check+=1

for i in range(len(final)):
    if final[i]==fake:
        count = i

if check==1:
    print(chr(65+count))
else:
    print('?')