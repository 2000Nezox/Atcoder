N = int(input())
x = 0
result = False
while x < 100:
    d = 0
    sum = 0
    while sum <= N:
        sum = 4*x + 7*d
        if sum == N:
            result = True
            break
        d += 1
    if result == True:
        break
    x += 1

if result == True:
    print("Yes")
else :
    print("No")
