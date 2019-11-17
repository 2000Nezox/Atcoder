ab = list(map(int,input().split(' ')))
ans = sum(ab)/2
if ans.is_integer():
    print(int(ans))
else:
    print('IMPOSSIBLE')