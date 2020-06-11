A,B = map(int,input().split(' '))
B = B*2
if A <= B:
    print(0)
else:
    print(A-B)