N = int(input())
lst = [list(map(str,input())) for i in range(N)]
ans = []
for i1 in range(N):
    tmp = []
    for i2 in range(N):
        tmp.append(lst[i2][i1])
    tmp = tmp[::-1]
    ans.append(tmp)

[print(''.join(i)) for i in ans]