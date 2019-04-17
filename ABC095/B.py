N,X = map(int,input().split())
m =[]
count = N
for n in range(N):
    m.append(int(input()))

X = X-sum(m) #残りはX


while True:
    if X >= min(m):
        X -= min(m)
        count += 1
    else:
        break

print(count)
