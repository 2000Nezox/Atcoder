N = int(input())
D = []
for d in range(N):
    D.append(input())

D = list(set(D))
D.sort()
print(len(D))
