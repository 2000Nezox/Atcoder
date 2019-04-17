a,b = map(int,input().split())

count = 0
count += a-1
if b >= a:
    count +=1

print(count)
