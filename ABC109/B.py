def is_unique(seq):
    return len(seq) == len(set(seq))


n = int(input())
w = []
for i in range(n):
    w.append(input())

first = w[0][-1]
result = "Yes"
if not is_unique(w):
    result = "No"
else:
    for i in range(1,len(w)):
        if not w[i][0] == first:
            result = "No"
            break
        first = w[i][-1]

print(result)
