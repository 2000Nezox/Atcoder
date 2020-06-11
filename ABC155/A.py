import sys
lst = list(map(int,input().split()))
lst1 = list(set(lst))
ans = False
if len(lst1) == 1:
    print('No')
    sys.exit()
if lst.count(lst1[0]) == 1:
    if lst.count(lst1[1]) == 2:
        ans = True
else:
    if lst.count(lst1[1]) == 1:
        ans = True

if ans == True:
    print('Yes')
else:
    print('No')