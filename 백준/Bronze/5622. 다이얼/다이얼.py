name = input()
sum= 0

for i in range(len(name)):
    if name[i]==chr(65) or name[i]==chr(66) or name[i]==chr(67):
        sum+=3
    #A B C
    elif name[i]==chr(68) or name[i]==chr(69) or name[i]==chr(70):
        sum+=4
    #D E F
    elif name[i]==chr(71) or name[i]==chr(72) or name[i]==chr(73):
        sum+=5
    #G H I
    elif name[i]==chr(74) or name[i]==chr(75) or name[i]==chr(76):
        sum+=6
    #J K L
    elif name[i]==chr(77) or name[i]==chr(78) or name[i]==chr(79):
        sum+=7
    #M N O
    elif name[i]==chr(80) or name[i]==chr(81) or name[i]==chr(82) or name[i]==chr(83):
        sum+=8
    #P Q R S 
    elif name[i]==chr(84) or name[i]==chr(85) or name[i]==chr(86):
        sum+=9
    #T U V
    elif name[i]==chr(87) or name[i]==chr(88) or name[i]==chr(89) or name[i]==chr(90):
        sum+=10
    #W X Y Z
print(sum)
    