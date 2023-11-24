import sys

n, m = map(int, input().split())

arr = []

def answer():
    for i in arr:
        print(i, end = " ")
    print()

def choose(current_num):
    if current_num == m + 1:
        answer()
        return

    for i in range(1, n + 1):
        arr.append(i)
        choose(current_num + 1)
        arr.pop()
    
    return

choose(1)