ans = 0
for i in range(1,50000+1):
    i1 = str(i)
    # print(type(i1))
    # print(i1)
    if i % 3 == 0 or '3' in i1:
    # if '3' in i1:
        ans = ans + i
        print(i)
print(ans)