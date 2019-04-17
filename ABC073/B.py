n = int(input())
ans = []
for i in range(n):
    l,r = map(int,input().split())
    ans.append(r-l+1)
print(sum(ans))
