lst = []
while True:
    tmp = list(map(int, input().split()))
    if tmp[0] == tmp[1] == 0:
        break
    else:
        lst.append(tmp)

for i in lst:
    i.sort()
    print(i[0], i[1])
