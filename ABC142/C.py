N = input()
A = list(map(int,input().split()))
A_len = [*range(len(A))]
# A1 = []
# A1 = [[A[i],i] for i in range(len(A))]
A1 = sorted(A_len, key=lambda i: -A[i])
A2 = [A[i] for i in A1]
print(A1,A2)