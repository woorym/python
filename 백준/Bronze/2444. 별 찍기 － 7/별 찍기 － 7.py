num = int(input())


for j in range(1, num):
    print(" " * (num - j) + "*" * j, end = "")
    print("*" * (j - 1))
    # print("*" * (j - 1)+ " " * (num - j))
    
for j in range(1, num + 1):
    print(" " * (j - 1) + "*" * (num - j + 1), end = "")
    print("*" * (num - j))
    # print("*" * (num - j) + " " * (j - 1))
