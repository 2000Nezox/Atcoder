K,X = map(int,input().split(' '))
min = X - K + 1
max = X + K - 1
ans = list(range(min,max+1))
result = ''
for i in ans:
    result += str(i) + ' '
print(result)