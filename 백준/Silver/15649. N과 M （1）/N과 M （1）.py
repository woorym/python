n, m = map(int, input().split())

arr = []
check = 1

def print_answer():
   for i in arr:
      print(i, end = " ")
   print()

def choose(current_num):
   if current_num == m + 1:
      print_answer()
      return

   for i in range(1, n + 1):
      if i not in arr:
         arr.append(i)
         choose(current_num + 1)
         arr.pop()

choose(1)