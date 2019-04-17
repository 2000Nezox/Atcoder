N,M = map(int,input().split())
K = []
ans = 0
for n in range(N):
    K.append(list(map(int,input().split())))

for m in range(1,M+1):
    for k in K:
        if not m in k[1:]:
            break
    else :
        ans += 1

print(ans)
