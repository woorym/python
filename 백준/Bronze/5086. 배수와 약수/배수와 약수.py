try:
    while True:
        a, b = list(map(int, input().split()))

        if a == 0 and b == 0:
            break
        elif b % a == 0:
            print("factor")
        elif a % b == 0:
            print("multiple")
        elif not (b % a == 0 and a % b == 0):
            print("neither")
except:
    exit()