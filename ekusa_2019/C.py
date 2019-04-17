n,q = map(int,input().split())
s = list(input()) #ゴーレムの並び方を習得
t,d = [],[]
for i in range(q):
    t1,d1 = input().split()
    t.append(t1)
    d.append(d1)

for r in set(t):
    f = [i for i, x in enumerate(t) if x==r]
    for c in f:
        if d[f] == "L":
            l += 1
        else:
            r += 1
