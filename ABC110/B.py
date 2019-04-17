N,M,X,Y = map(int,input().split())
x = list(map(int,input().split()))
y = list(map(int,input().split()))
x.sort(reverse = True)
y.sort()

x_max = x[0]
y_min = y[0]
result = "War"
for z in range(X+1,Y+1):
    if x_max < z <= y_min:
        result = "No War"
        break

print(result)
