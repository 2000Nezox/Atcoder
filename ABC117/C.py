N,M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()

x = [num + abs(X[0]) for num in X]
print(x)
#間の距離
a = []
for i in range(M-1):
    a.append(X[i+1] - X[i])
a.sort(reverse = True)
print(a)

b = 0
for i in range(N-1):
    b += a[i]

c = X[M-1] - X[0]
print(c)

わからなかった！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！
