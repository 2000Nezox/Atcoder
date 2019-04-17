s = list(set(input()))
abc = [chr(i) for i in range(97, 97+26)]

for i in abc:
    if not s.count(i) == 1:
        ans = i
        break
else:
    ans = "None"

print(ans)
