A,B = map(int,input().split(' '))
ans = 0
outlet = 1
while outlet < B:
    outlet = outlet -1
    outlet = outlet + A
    ans = ans + 1
print(ans)