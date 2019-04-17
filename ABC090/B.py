import sys
A,B = map(int,input().split())

cunt = 0
if not 10000 <= A <= B <= 99999:
    print(0)
    sys.exit(0)
for i in range(A,B+1):
    sita = list(str(i))
    ue = sita[::-1]

    if sita == ue:
        cunt += 1

print(cunt)
