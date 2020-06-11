def next1(ii):
    if len(eimozi)-1 < ii:
        ii = 0
        return ii,eimozi[ii]
    return ii+1,eimozi[ii]

eimozi = [chr(i) for i in range(97, 97+26)]
lst = [['']*48 for i in range(48)]
x,y = 48,46
now = 0
x_y,y_x = 0,-1
while True:
    # try:
    for i in range(x):
        now, tmp = next1(now)
        lst[0][i] = tmp
    for i in range(y):
        now, tmp = next1(now)
        lst[i + 1][-1] = tmp
    for i in range(x, 0, -1):
        now, tmp = next1(now)
        lst[-1][i] = tmp
    for i in range(y, 1, -1):
        now, tmp = next1(now)
        lst[0][i] = tmp
    x_y = x_y + 1
    y_x = y_x - 1
    x = x-2
    y = y-2

    # except Exception as e:
    #     break
print(lst)



