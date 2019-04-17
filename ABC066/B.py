import math
s = input()
s = s[0:-2]
ans = 0
for i in range(len(s)):
    if not len(s)%2 == 0:
        s = s[0:-2]
        continue
    x  = math.floor(len(s)/2-1)
    if s[0:x] == s[x+1:-1]:
        ans = len(s)
        break
    s = s[0:-2]

print(ans)
