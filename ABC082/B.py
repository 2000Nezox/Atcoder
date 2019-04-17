s = input()
t = input()
s_asc = "".join(sorted(s))
t_dsc = "".join(sorted(t,reverse=True))
if s_asc < t_dsc:
    print("Yes")
else :
    print("No")
