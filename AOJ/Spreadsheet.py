r, c = map(int, input().split())
lst = []
for i in range(r):
    tmp = list(map(int, input().split()))
    tmp.append(sum(tmp))
    lst.append(tmp)

lstsum = []
for i in range(c+1):
    tmp = []
    for j in range(r):
        tmp.append(lst[j][i])
    lstsum.append(sum(tmp))

lst = [[str(i) for i in y] for y in lst]
lstsum = [str(i) for i in lstsum]
[print(' '.join(i)) for i in lst]
print(' '.join(lstsum))
