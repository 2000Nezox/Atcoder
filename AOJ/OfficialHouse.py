import copy

lst = []
tmp = [[0] * 10 for i in range(3)]
for i in range(4):
    lst.append(copy.deepcopy(tmp))

n = int(input())
for i in range(n):
    b, f, r, v = map(int, input().split())
    lst[b - 1][f - 1][r - 1] = lst[b - 1][f - 1][r - 1] + v

for i, data in enumerate(lst):
    for x in data:
        # x = [str(a) for a in x]
        print('', *x)

    if i != 3:
        print('#' * 20)
