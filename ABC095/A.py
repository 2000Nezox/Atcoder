S = list(input())
ans = 700
for i in range(len(S)):
    if S[i] == "o":
        ans += 100

print(ans)
