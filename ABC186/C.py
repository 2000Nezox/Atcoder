N = int(input())
count = 0
for i in range(1,N+1):
    tmp = str(i)
    tmp8 = str(oct(i))
    if '7' in tmp or '7' in tmp8:
        count = count + 1

print(N-count)