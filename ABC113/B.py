N = int(input())
T,A = map(int,input().split())
H = list(map(int,input().split()))

y = 1000

for i in range(N):
    x = A - (T - H[i] * 0.006)
    if y > abs(x):
        y = abs(x)
        result = i+1

print(result)
