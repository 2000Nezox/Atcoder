def add(x,y):
    return x + y


a,b = map(int,input().split())
x = b -a
sum = 1
next_x = 2
while True:
    result = add(sum,next_x)
    if result - sum == x:
        print(sum - a)
        break
    sum = result
    next_x += 1
