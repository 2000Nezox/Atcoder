D,N = map(int,input().split())

if N % 100 == 0:
    print((100**D)*(N+1))
else:
    print((100**D)*N)
