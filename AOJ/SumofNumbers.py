while True:
    tmp = input()
    if tmp == '0':
        break
    tmp = [int(i) for i in tmp]
    print(sum(tmp))
