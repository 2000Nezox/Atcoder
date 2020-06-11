N = int(input())
S = input()
lst = []
lst += ['b','abc','cabca']
tmp = 'cabca'
for i in range(100):
    tmp_lst = []
    tmp_lst.append('b'+tmp+'b')
    tmp_lst.append('a' + tmp_lst[0] + 'c')
    tmp_lst.append('c' + tmp_lst[1] + 'a')
    tmp = tmp_lst[-1]
    lst.extend(tmp_lst)
if S in lst:
    print(lst.index(S))
else:
    print(-1)
