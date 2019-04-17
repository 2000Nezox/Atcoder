h,w = map(int,input().split())
A = []
for i in range(h):
    A.append("#"+input()+"#")

print("#"*(w+2))
for i in A:
    print(i)
print("#"*(w+2))
