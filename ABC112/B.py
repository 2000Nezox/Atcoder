N,T = map(int,input().split())

cost = []
for n in range(N):
    c,t = map(int,input().split())
    if T >= t:
        cost.append(c)

if not cost:
    print("TLE")
else:
    cost.sort()
    print(cost[0])
