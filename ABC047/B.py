w,h,n = map(int,input().split())
p = [list(map(int,input().split())) for i in range(n)]

xmin,xmax,ymin,ymax = 0,w,0,h

for x,y,a in p:
    if a == 1:
        if x > xmin:
            xmin = x

    elif a == 2:
        if x < xmax:
            xmax = x

    elif a == 3:
        if y > ymin:
            ymin = y

    elif a == 4:
        if y < ymax:
            ymax = y

if xmax-xmin < 0 or ymax-ymin < 0:
    print(0)
else:
    print((xmax-xmin) * (ymax-ymin))
