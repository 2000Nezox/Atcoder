Str = input()
q = int(input())
for i in range(q):
    tmp = list(input().split())
    newtmp = []
    for i in tmp:
        if str.isdecimal(i):
            newtmp.append(int(i))
        else:
            newtmp.append(i)
    order, start, end = newtmp[0], newtmp[1], newtmp[2]
    if order == 'print':
        print(Str[start:end + 1])
    elif order == 'reverse':
        a = Str[start:end + 1:]
        a = a[::-1]
        Str = Str[0:start] + a + Str[end + 1:]

        # print(Str)
    else:
        Str = Str[0:start] + newtmp[3] + Str[end + 1:]
