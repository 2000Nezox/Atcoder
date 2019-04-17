S = list(input())

ans = 1000
for i in range(len(S)-2):
    sum = ""
    x = S[i:i+3]
    for i1 in x:
        sum += i1
    sum = int(sum)
    y = abs(753 -sum)
    if ans >= y:
        ans = y

print(ans)
