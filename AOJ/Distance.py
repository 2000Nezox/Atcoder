import math
lst = list(map(float,input().split()))
ans = math.sqrt((lst[2]-lst[0])**2 + (lst[3]-lst[1])**2 )
print(round(ans,8))
