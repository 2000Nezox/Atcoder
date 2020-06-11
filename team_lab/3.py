lst = [[1,1/1]]
count = 0
while True:
    tmp = lst[count]
    tmp[0] = tmp[0] + 1
    tmp[1] = tmp[1] + (1/tmp[0])
    if tmp[1] >= 15:
        print(tmp[0])
        break
    # print(tmp)
    lst.append(tmp)
