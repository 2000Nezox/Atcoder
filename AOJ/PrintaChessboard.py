while True:
    H, W = map(int, input().split())
    if H == W == 0:
        break
    else:
        for i in range(H):
            if i % 2 == 0:
                for i1 in range(W):
                    if i1 % 2 == 0:
                        print('#', end='')
                    else:
                        print('.', end='')
                print('')
            else:
                for i1 in range(W):
                    if i1 % 2 == 0:
                        print('.', end='')
                    else:
                        print('#', end='')
                print('')
        print('')
