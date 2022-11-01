H, M = map(int, input().split())

if H>=1 and M<45:
    print('%d %d' %(H-1, M+15))
elif H<1 and M>=45:
    print('%d %d' %(H,M-45))

elif H<1 and M<45:
    print('23 %d' %(M+15))

elif H>=1 and M>=45:
    print("%d %d" %(H,M-45))
