N,M = map(int,input().split())
A = [[x for x in input()] for i in range(N)]
B = [[x for x in input()] for i in range(M)]
result = "No"


for i in range(N-M+1):
    for j in range(N-M+1):
        result = True
        for k in range(M):
            for l in range(M):
                if A[i+k][j+l] != B[k][l]:
                    result = False
        if result:
            print("Yes")
            exit()




print("No")


