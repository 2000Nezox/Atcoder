N = int(input())
D = list(map(int,input().split(' ')))
ans = 0
for i in range(len(D)):
    for i1 in range(i,len(D)):
        if i== i1:
            continue
        ans = ans + (D[i] * D[i1])
print(ans)

