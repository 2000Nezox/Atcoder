N = int(input())
K = int(input())
X = int(input())
Y = int(input())

if K < N:
    ans = K * X
    ans = ans + (N-K) * Y
    print(ans)
else:
    ans = N * X
    print(ans)
