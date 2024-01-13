#백준 9935번
import sys
input = sys.stdin.readline

stack = []

string = input().rstrip()
bomb = input().rstrip()
length = len(bomb)

# print(string)
cnt = 0

for str in string:
    cnt += 1
    stack.append(str)
    if str == bomb[-1]:
        a = ""
        # print(stack[-(length) :])
        for i in stack[-(length) :]:
            a += i    
        
        # print(f"str {cnt}: {a}")
        if a == bomb:
            for _ in range(length):
                stack.pop()

# print(stack)
if len(stack) == 0:
    print("FRULA")
else:
    for i in stack:
        print(i, end = "")
