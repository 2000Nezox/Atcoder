N = int(input())
n =list(str(N))
sum = 0
for i in range(len(n)):
    sum += int(n[i])

if N % sum == 0:
    print("Yes")
else:
    print("No")
