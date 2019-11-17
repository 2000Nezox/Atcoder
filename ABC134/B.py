N,D = map(int,input().split(' '))
d = D*2+1
for i in range(1,20):
    if N <= d*i:
        print(i)
        exit()