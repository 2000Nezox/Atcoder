w = input()
W = list(set(w))
for i in W:
    if w.count(i)%2 == 0:
        continue
    else:
        print("No")
        exit()
print("Yes")