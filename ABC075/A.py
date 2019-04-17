a = input().split()
b = list(range(-100,101))

for i in b:
    if a.count(str(i)) == 1:
        print(i)
        break
