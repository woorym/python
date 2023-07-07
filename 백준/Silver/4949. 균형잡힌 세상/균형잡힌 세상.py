import sys

input = sys.stdin.readline

data = True

while True:
    try:
        stack = []
        check = 0

        data = list(input())
        if data[0] == '.':
            break
        
        for element in data:
            if element == '(' or element == '{' or element == '[':
                stack.append(element)
            
            if element == ')':
                if stack[-1] == '(':
                    stack.pop()
                else:
                    check = 1
                    break
            
            elif element == '}':
                if stack[-1] == '{':
                    stack.pop()
                else:
                    check = 1
                    break
            
            elif element == ']':
                if stack[-1] == '[':
                    stack.pop()
                else:
                    check = 1
                    break
            
            elif element == '.':
                break

        if check == 0 and len(stack) == 0:
            print("yes")

        else:
            print("no")
    except:
        print('no')
        continue
        
