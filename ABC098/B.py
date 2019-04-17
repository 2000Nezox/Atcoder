N = int(input())
S = list(input())

count = []

if len(S) == 2:
    if S[0] == S[1]:
        count.append(1)
    else:
        count.append(0)
else:
    for i in range(1,N-1):
        sum = 0
        sita = S[0:i]
        usiro = S[i:N]

        #print(sita,usiro)
        sita = list(set(sita))
        usiro = list(set(usiro))

        #print(sita,usiro)
        for x in range(len(sita)):
            if sita[x] in usiro:
                sum += 1

        count.append(sum)

print(max(count))
