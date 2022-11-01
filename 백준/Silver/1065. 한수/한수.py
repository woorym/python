
n=int(input())

cnt=0
for i in range(1,n+1):
	if i<100:
		cnt+=1
		continue
	hund=i//100
	ten=(i//10)%10
	one=i%10
	if hund-ten==ten-one:
		cnt+=1

print(cnt)