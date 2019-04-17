a,b  = map(int,input().split())
result = "No"
c = [1,2,3]
for i in c:
    if (a*b*i)%2 == 1:
        result = "Yes"
        break

print(result)
