N,Q = map(int,input().split(' '))
lst = [list(map(int,input().split(' '))) for i in range(Q)]
ans = [0] * N
for i in lst:
    for i1 in range(i[0]-1,i[1]):
        ans[i1] = i[2]
[print(i) for i in ans]