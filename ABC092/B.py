N = int(input())
D,X = map(int,input().split())
A = []
for n in range(N):
    A.append(int(input()))

sum = 0
for n in range(N):    #ここで人数
    sum += 1
    for d in range(1,D+1):#ここで日数
        result = A[n] * d + 1
        if result <= D:
            sum += 1

sum = X + sum

print(sum)
