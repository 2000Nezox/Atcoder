n = int(input())
ans = 10000000000000
for i in range(400):
    for i1 in range(400):
        if i * i1 > n:
            break
        tmp = i * i1
        sa1 = max(i,i1) - min(i,i1)
        sa2 = n - tmp
        if sa1+sa2 < ans:
            ans = sa1+sa2
        if ans == 0:
            print(0)
            exit()
print(ans)

