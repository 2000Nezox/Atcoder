x1,y1,x2,y2 = list(map(int,input().split()))

a = x2-x1
b = y2-y1
y3 = y2 + a
x3 = x2 - b
y4 = y3 -b
x4 = x3 -a

print(x3,y3,x4,y4)
