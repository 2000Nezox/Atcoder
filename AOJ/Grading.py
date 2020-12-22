while True:
    m, f, r = map(int, input().split())
    if m == f == r == -1:
        break
    tmp = m + f
    if m == -1 or f == -1 or tmp < 30:
        print('F')
    elif tmp >= 80:
        print('A')
    elif tmp >= 65:
        print('B')
    elif tmp >= 50 or ((30 <= tmp < 50) and r >= 50):
        print('C')
    else:
        print('D')
