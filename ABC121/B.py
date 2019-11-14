N,M,C = map(int,input().split(' '))
B = list(map(int,input().split(' ')))
A = [input().split(' ') for i in range(N)]
result = 0
for i in range(N):
    ans = 0
    for x in range(M):
        ans = ans + (int(A[i][x]) * B[x])
    if ans + C > 0:
        result = result + 1

print(result)