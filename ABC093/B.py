A,B,K = map(int,input().split())

if B-A+1 <= K * 2:
    for i in range(A,B+1):
            print(i)

else:
    for i in range(A,A+K): #AからB
        print(i)

    for i in range(B-K+1,B+1):
        print(i)
