n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
p = a[0]-1
result = False
ans = 1

if a[0] == 2:
    result = True
else:
    for i in range(10**5):
        if a[p] == 2:
            ans += 1
            result = True
            break
        else:
            p = a[p]-1
            ans += 1

if result == True:
    print(ans)
else:
    print("-1")
