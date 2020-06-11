import sys
N = int(input())
s_lst = []
for i in range(N):
    s_lst.append(input())

S_lst = list(set(s_lst))
if len(S_lst) == len(s_lst):
    s_lst.sort()
    [print(i) for i in s_lst]
    sys.exit()
tmp,ans = 0,[]
for i in S_lst:
    if s_lst.count(i) > tmp:
        ans.clear()
        ans.append(i)
        tmp = s_lst.count(i)
    elif s_lst.count(i) == tmp:
        ans.append(i)

ans.sort()
[print(i) for i in ans]