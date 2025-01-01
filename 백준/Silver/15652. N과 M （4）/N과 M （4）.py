import sys
# input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

def print_answer():
    for i in arr:
        print(i, end = " ")
    return
    
    
def again(current):
    
    if current == m + 1:
        print_answer()
        print()
        return
    
    for i in range(1, n + 1):
        if len(arr) != 0 and arr[-1] > i:
            continue
        arr.append(i)
        again(current + 1)
        arr.pop()
        
again(1)