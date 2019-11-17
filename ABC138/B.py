N = int(input())
A = list(map(int,input().split(' ')))
lst = []
for i in range(N):
    lst.append(1/A[i])
print(1/sum(lst))