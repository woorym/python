a= int(input())
b= int(input())
c= int(input())

result= a*b*c

k = str(result)

for i in range(10):
    print('%d' %int(k.count(str(i))))