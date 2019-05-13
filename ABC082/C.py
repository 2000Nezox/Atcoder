n = int(input())
a = list(map(int,input().split()))
ans = 0
b = list(set(a))
for i in b:
    if not a.count(i) == i:
        d = a.count(i)
        # print(d-i,d,i-d)
        if d > i:
            ans += d-i
        else:
            if i - d > i:
                ans += i-d
            else:
                ans += d
print(ans)
