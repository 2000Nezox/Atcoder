S = list(input())
S = [int(i) for i in S]
sum1,sum2 = 0,0
for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == 0:
            sum1 += 1
    else:
        if S[i] == 1:
            sum1 += 1

for i in range(len(S)):
    if i % 2 == 0:
        if S[i] == 1:
            sum2 += 1
    else:
        if S[i] == 0:
            sum2 += 1
if sum1 <= sum2:
    print(sum1)
else:
    print(sum2)
