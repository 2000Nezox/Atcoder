N = int(input())
A = list(map(int,input().split(' ')))
B = list(map(int,input().split(' ')))
C = list(map(int,input().split(' ')))
tmp = 60
ans = 0
for i in A:
    ans = ans + B[i-1]
    if i-1 == tmp:
        ans = ans + C[i-2]
    tmp = i
print(ans)