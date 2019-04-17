x,a,b = map(int,input().split())

a_ans = abs(x-a)
b_ans = abs(x-b)
if a_ans < b_ans:
    print("A")
else:
    print("B")
