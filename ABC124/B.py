N = int(input())
H = list(map(int,input().split()))
ma = 0
ans = 0

for i in H:
    if ma <= i:
        ans += 1
        ma = i


print(sum)
