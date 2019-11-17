N = int(input())
p = list(map(int,input().split(' ')))
p1 = p.copy()
p1.sort()
for i in range(N):
    for i1 in range(i,N):
        p2 = p.copy()
        p2[i],p2[i1] = p2[i1],p2[i]
        if p2 == p1:
            print("YES")
            exit()
print("NO")
