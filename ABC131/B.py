N,L = map(int,input().split(' '))
lst = [i+L-1 for i in range(1,N+1)]
normal_ans = sum(lst)
count = 10000000
result = 0
for i in range(len(lst)):
    ans_lst =  lst.copy()
    del ans_lst[i]
    special_ans = sum(ans_lst)
    # print(special_ans,normal_ans-special_ans)
    if count >= abs(normal_ans-special_ans):
        count = abs(normal_ans-special_ans)
        result = special_ans
print(result)
