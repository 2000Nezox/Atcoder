S = list(input())
ki = ["R","U","D"]
gu = ["L","U","D"]
for i in range(len(S)):
    tmp = S[i]
    if (i+1) % 2 == 1:
        if "R" == tmp or "U" == tmp or "D" == tmp:
            continue
        print("No")
        exit()
    else:
        if "L" == tmp or "U" == tmp or "D" == tmp:
            continue
        print("No")
        exit()
print("Yes")