A = [int(input()) for i in range(5)]
k = int(input())
ans = 0
for i in range(5):
    for x in range(i,5):
        if A[x] - A[i] > k:
            ans = ans + 1
if ans > 0:
    print(":(")
else:
    print("Yay!")