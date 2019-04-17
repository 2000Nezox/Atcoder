def f(i):
    if i%2 == 0:
        return int(i/2)
    else:
        return 3*i+1


s = int(input())
a = [s]
ans = 0
for i in range(1,1000000):
    ai = f(a[i -1])
    if a.count(ai) == 1:
        ans = i + 1
        break
    a.append(ai)
print(ans)
