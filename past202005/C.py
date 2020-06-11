A,R,N = map(int,input().split())
ans = A*(R**(N-1))
if ans >= 10**9:
    print('large')
else:
    print(ans)