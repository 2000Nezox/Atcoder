N,M,X = map(int,input().split())
A = list(map(int,input().split()))

first = X
last = N+1-X
first_count = 0
last_count = 0

for a in range(len(A)):
    if X < A[a]:
        first_count += 1
    else:
        last_count += 1

if first_count > last_count:
    ans = last_count
else :
    ans = first_count

print(ans)
