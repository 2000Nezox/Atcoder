import re
A,B = list(map(int,input().split()))
S = input()

d = re.compile("\d+")

if (d.match(S[:A])) and S[A] == "-" and d.match(S[A+1:]):
    print("Yes")

else:print("No")
