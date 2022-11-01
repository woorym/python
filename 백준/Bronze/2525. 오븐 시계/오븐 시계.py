from calendar import c


h,m =map(int, input().split())
c = int(input())


k = 60*h +m + c
a = k//60

if k//60>=24:
    print("%d %d" %(k//60-24,k-(a*60)))

else:
    print("%d %d" %(k//60,k-(a*60)))
