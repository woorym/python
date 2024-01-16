#백준 17298번
import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().    split()))
arr.reverse()
# print(arr)
stack = []
result = []

for i in arr:
    while stack:
        if stack[-1] <= i:
            stack.pop()
        else:
            result.append(stack[-1])
            break
        
    if len(stack) == 0:
        result.append(-1)
    stack.append(i)

# print(result)
result.reverse()
# print(result)
print(" ".join(map(str, result)))    
