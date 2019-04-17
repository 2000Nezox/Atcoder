import math
N = int(input())
p = []
for i in range(N):
    p.append(int(input()))

p.sort(reverse=True)
p[0] /= 2
sum = 0
for i in p:
    sum += i

print(math.floor(sum))
