A = list(map(int,input().split()))
A.sort()

cost = A[1] -A[0]
cost +=  A[2] - A[1]

print(cost)
