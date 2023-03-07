score_list = []
total = 0
score_dict = {'A+' : 4.5, 'A0' : 4.0, 'B+' : 3.5, 'B0' : 3.0, 'C+' : 2.5, 'C0' : 2.0, 'D+' : 1.5, 'D0' : 1.0, 'F' : 0.0}

for _ in range(20):
    arr = list(map(str, input().split()))
    
    if arr[2] == 'P':
        continue

    result = float(arr[1]) * score_dict[arr[2]] 
    score_list.append(result)
    total += float(arr[1])


sum = 0

for i in score_list:
    sum += i

print(f'{sum / total : .6f}')
