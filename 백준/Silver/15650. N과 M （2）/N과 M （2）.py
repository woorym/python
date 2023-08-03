n, m = map(int, input().split())

arr = []

# def print_answer():
   # for i in arr:
      # print(i, end = " ")
   # print()
# 
def choose(current_num):
   if len(arr) == m:
      # print_answer()
      print(' '.join(map(str, arr)))
      return

   for i in range(current_num, n + 1):
      if i not in arr:
         arr.append(i)
         choose(i + 1)
         arr.pop()

choose(1)