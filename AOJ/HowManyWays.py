n, x = map(int, input().split())
lst = []
for i in range(1, n + 1):
    for i1 in range(1, n + 1):
        tmp = i + i1
        ans = x - tmp
        if ans <= 0:
            continue
        elif i != i1 and i1 != ans and ans != i:
            lst.append([i, i1, ans])

[i.sort() for i in lst]
lst.sort()
lst = list(map(list, set(map(tuple, lst))))
print(len(lst))
