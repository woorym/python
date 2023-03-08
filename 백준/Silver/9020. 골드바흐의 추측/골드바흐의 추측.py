# import sys

def primary_number(n):
    root = int(n ** 0.5 + 1)
    for i in range(2, root):
        if n % i == 0:
            return 0
    
    return n
    

times = int(input())
# ary = []
ary = [0]
for _ in range(times):

    num = int(input())

    number = num // 2
    # max = sys.maxsize
    max = 10000

    while number <= num:
    
        if primary_number(number) == 0:
            number += 1
            continue

        check = num - primary_number(number)
        if primary_number(check) != 0:
            ls = [number, check]
            break        
            # dif = abs(number - check)
            # if max > dif:
            #     max = dif
                # ls = [number, check]
                # ary[0] = [number, check]
                # ary.append([number, check])


        number += 1
    # ary.append(ls)
    ary[0] = ls

# # print(ary)
# for ls in ary:
#     print(ls[0], ls[1])
    if ary[0][0] < ary[0][1]:
        print(ary[0][0], ary[0][1])
    else:
        print(ary[0][1], ary[0][0])