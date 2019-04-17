def word_rotation(s):
    s.insert(0,s.pop())

S = list(input())
T = list(input())

for i in range(len(S)):
    word_rotation(S)
    if S == T:
        print("Yes")
        break
else:
    print("No")
