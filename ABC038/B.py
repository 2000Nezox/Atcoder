lst1 = list(map(int,input().split(' ')))
lst2 = list(map(int,input().split(' ')))

for i in lst1:
    if lst2.count(i) >= 1:
        print("YES")
        exit()
print("NO")

