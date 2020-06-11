N = int(input())
S = list(input())
count = 1
tmp = S[0]
for i in range(1,N):
    if tmp == S[i]:
        continue
    else:
        tmp = S[i]
        count = count + 1
print(count)