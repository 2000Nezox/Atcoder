n,k = map(int,input().split())
sum = k
for i in range(n-1):
    sum *= k-1

print(sum)
