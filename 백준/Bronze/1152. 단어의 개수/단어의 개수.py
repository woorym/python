name = input()

count = name.split(' ')
result = len(count)


if count[0]=='':
    result -=1


if count[len(count)-1]=='':
    result -=1


print(result)