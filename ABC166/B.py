N,K = map(int,input().split(' '))

sunuke = [1] * N

for i in range(K):
    di = int(input())
    tmp = map(int, input().split())
    for t in tmp:
        sunuke[t - 1] = 0

print(sum(sunuke))