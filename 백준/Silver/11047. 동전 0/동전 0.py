import sys

input = sys.stdin.readline

n, k = map(int, input().split())

coin_val = {}
coin_list = []
for _ in range(n):
    coin = int(input())
    coin_list.append(coin)

for coin_in in reversed(coin_list):
    coin_val[coin_in] = 0

check = k

for key in coin_val.keys():
    if check >= key:
        num1 = check // key
        check = check % key
        coin_val[key] = num1

sum = 0
for item in coin_val.values():
    sum += item

print(sum)