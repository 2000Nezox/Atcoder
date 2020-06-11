S = list(input())
for i in range(len(S)-1):
    S1 = S[i]
    S2 = S[i+1]
    if S1 == S2:
        print("Bad")
        exit()
print("Good")