def judge0(icon1, lst):
    if not lst:
        for i in range(1, 14):
            print(icon1, i)
    else:
        [print(icon1, x) for x in range(1, 14) if not (x in lst)]


n = int(input())
S, H, C, D = [], [], [], []
for i in range(n):
    icon, number = input().split()
    if icon == 'S':
        S.append(int(number))
    elif icon == 'H':
        H.append(int(number))
    elif icon == 'C':
        C.append(int(number))
    else:
        D.append(int(number))

judge0('S', S)
judge0('H', H)
judge0('C', C)
judge0('D', D)
