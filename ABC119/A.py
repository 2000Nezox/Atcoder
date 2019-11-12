S = list(map(int,input().split("/")))
ans = False
if S[0] > 2019:
    ans = True
elif S[0] >= 2019 and S[1] > 4:
    ans = True
elif S[0] >= 2019 and S[1] >= 4 and S[2] > 30:
    ans = True

if ans == True:
    print("TBD")
else:
    print("Heisei")