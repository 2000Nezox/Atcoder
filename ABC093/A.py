import sys
S = input()
abc = list("abc")

for i in range(len(abc)):
    if abc[i] in S:
        continue
    else :
        print("No")
        sys.exit(0)

print("Yes")
