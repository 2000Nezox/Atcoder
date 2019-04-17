n,k = map(int,input().split())
l = list(map(int,input().split()))
l.sort(reverse=True)
a = 0

for i in range(k):
    a+= l[i]
print(a)
