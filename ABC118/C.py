N = int(input())

A = list(map(int,input().split()))
i = 0
while True:
    A.sort()
    for a in range(len(A)-1):
        if not(A[a] == 0) and A[a+1] % A[a] == 0:
                A[a+1] = A[a+1] % A[a]
        else:
            A[a+1] = A[a+1] - A[a]

    A = [i for i in A if  i > 0]
    if len(A) == 1:
        break

print(A[0])
