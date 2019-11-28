import math
A, B, X = map(int, input().split(' '))
max = 1000000000
min = 0
ans = 0
if X > A * max + B * len(str(max)):
    print(max)
    exit()


while True:
    tmp = (max - min) / 2 + min
    tmp1 = A * tmp + B * len(str(int(tmp)))

    if tmp == ans:
        print(int(ans))
        exit()

    # print(tmp)
    if tmp1 <= X:
        min = tmp
    if tmp1 >= X:
        max = tmp
    ans = tmp