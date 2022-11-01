check=0
name = input()
i=0
ary = ['c=','c-','dz=','d-','lj','nj','s=','z=']
ary1=[]

while check!=2:
    count = 0
    try:
        if name[i]+name[i+1] in ary:
            ary1.append(name[i]+name[i+1])
            i+=1
        else:
            count+=1
    except:
        count+=1
    try:
        if name[i]+name[i+1]+name[i+2] in ary:
            ary1.append(name[i]+name[i+1]+name[i+2])
            i+=2
        else:
            count+=1
    except :
        count+=1
    try:
        if count==2:
            ary1.append(name[i])
        i+=1
    except :
        check=2
        break

print(len(ary1))