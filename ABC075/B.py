H,W = map(int,input().split(' '))
N = [[i for i in input()] for i in range(H)]
lst = [-1,0,1]
for i in range(H):
    for x in range(W):
        if N[i][x] == '.':
            ans = 0
            for i1 in lst:
                for x1 in lst:
                    if (i+i1 >= 0 and x+x1 >= 0) and (i+i1 < H and x+x1 < W):
                        if N[i+i1][x+x1] == "#":
                            ans = ans + 1
            N[i][x] = ans

[print(''.join([str(x) for x in i])) for i in N]
