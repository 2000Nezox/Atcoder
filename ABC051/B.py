import numba import jit
k,s = map(int,input().split())
ans = 0
i = list(range(k+1))

for x in i:
    for y in i:
        z = s-x-y
        if 0 <= z <= k:
            ans += 1
print(ans)
