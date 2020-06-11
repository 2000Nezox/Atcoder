N,M = map(int,input().split(' '))
a = [list(map(int,input().split(' '))) for i in range(N)]
c = [list(map(int,input().split(' '))) for i in range(M)]
last_ans = []
for i in range(len(a)):
    middle_ans = []
    for i1 in range(len(c)):
        tmp_a = a[i]
        tmp_c = c[i1]
        # print(tmp_a,tmp_c,abs(tmp_a[0]-tmp_c[0]))
        tmp = abs(tmp_a[0]-tmp_c[0]) + abs(tmp_a[1]-tmp_c[1])
        middle_ans.append(tmp)
    # rint(middle_ans,"aaaa")p
    last_ans.append(middle_ans.index(min(middle_ans))+1)
[print(i) for i in last_ans]