W,a,b = map(int,input().split())

if a+W < b:
    result = b-(a+W)
elif a > b+W:
    result = a-(b+W)
else:
    result = 0

print(result)
