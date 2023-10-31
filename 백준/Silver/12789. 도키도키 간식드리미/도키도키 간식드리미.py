import sys

input = sys.stdin.readline
n = int(input())
line = list(map(int, input().split()))
stack = []
ps = 1
for i in line:
	stack.append(i)
	while stack and stack[-1] == ps:
		stack.pop()
		ps += 1
	if len(stack) > 1 and stack[-1] > stack[-2]:
		print("Sad")
		sys.exit()
if stack:
	print("Sad")
else:
	print("Nice")