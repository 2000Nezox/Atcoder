A,B,C = map(int,input().split(' '))
ans = A*B*C
print(ans%(10**9+7))