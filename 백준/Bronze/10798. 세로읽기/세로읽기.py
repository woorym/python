arr = [
    list(input())
    for _ in range(5)
]

max = len(arr[0])
for i in range(5):
    if max < len(arr[i]):
        max = len(arr[i])

result = ""
for i in range(max):
    for j in range(5):
        try:
            result += arr[j][i]
        
        except:
            pass

print(result)