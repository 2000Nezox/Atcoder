N = int(input())
S = input()
if N == 1:
    print("No")
    exit()

for i in range(1,N):
    s1 = S[:i]
    s2 = S[i:]
    if s1 == s2 and len(s1)*2 == N:
        print("Yes")
        exit()
print("No")