n, m = list(map(int, input().split()))

know_name = []
dont_know_name = []

for _ in range(n):
    name = input()
    know_name.append(name)

for _ in range(m):
    who = input() 
    dont_know_name.append(who)


check_name = list(set(dont_know_name) & set(know_name))

check_name.sort() 

print(len(check_name))
for i in check_name:
    print(i)
