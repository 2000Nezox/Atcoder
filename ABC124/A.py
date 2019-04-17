A,B = map(int,input().split())
sum = 0
for i in range(2):
    if A < B:
        sum += B
        B -= 1
    else:
        sum += A
        A -= 1

print(sum)
