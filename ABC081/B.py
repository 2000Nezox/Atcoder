N = input()
A = list(map(int,input().split()))
res = 0
while True:
    result = 0
    for i in A:
        if i%2:
            result = 1
    if result:
        break

    A = [i/2 for i in A]
    res += 1

print(res)
