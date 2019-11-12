import bisect
N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
C = list(map(int,input().split()))
ans = 0
A.sort()
C.sort()
B.sort()

for i in B:
    a = bisect.bisect_left(A,i)
    c = bisect.bisect_right(C,i)
    ans += a*(N-c)

print(ans)
