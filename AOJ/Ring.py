s = input()
p = input()
start = s.index(p[0])
if start != 0:
    s = s[start:] + s[0:start]
count = 0
for i in range(len(s)):
    print(s[i], p[count])
    if s[i] == p[count]:
        count = count + 1

print(count,len(p))
if count == len(p):
    print('Yes')
else:
    print('No')
