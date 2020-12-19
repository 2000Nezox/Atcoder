ans = 0
a, b, c = map(int, input().split())
for i in range(a, b + 1):
    if c % i == 0:
        ans = ans + 1

print(ans)
