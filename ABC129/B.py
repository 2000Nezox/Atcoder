N = int(input())
W = list(map(int,input().split()))
ans = 100000000000
for i in range(100):
    tmp = []
    tmp.append(abs(sum(W[:i])))
    tmp.append(abs(sum(W[i:])))
    tmp.sort()
    if tmp[1]-tmp[0] < ans:
        ans = tmp[1]-tmp[0]
print(ans)
