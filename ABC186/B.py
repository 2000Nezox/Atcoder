lst = []
min1 = 1000000000000000000000000000000000000000
sum1 = 0
H, W = map(int, input().split())
for i in range(H):
    tmp = list(map(int, input().split()))
    lst.append(tmp)

for i in lst:
    tmp = min(i)
    if min1 > tmp:
        min1 = tmp
for i in lst:
    sum1 = sum1 + sum(i)

print(sum1 - (H * W * min1))
