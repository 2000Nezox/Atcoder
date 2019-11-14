lst = [int(input()) for i in range(5)]
i1,i2 = 0,0
for i,x in enumerate(lst):
    i3 = 10 - (x % 10)
    if i3 >= i1 and not(i3 == 10):

        i1 = i3
        i2 = i


lst.append(lst.pop(i2))

ans = 0
for i in range(4):

    if lst[i] % 10 == 0:
        ans = ans + lst[i]

    else:
        ans = ans + ((lst[i] // 10 + 1)*10)


print(ans+lst[-1])