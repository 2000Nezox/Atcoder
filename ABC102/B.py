N = int(input())
A = list(map(int,input().split()))


A.sort()
result = A[len(A)-1] - A[0]
print(abs(result))
