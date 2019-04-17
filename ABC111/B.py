N = int(input())

for i in range(N,999+1):
    n = list(str(i))
    if n.count(n[0]) == 3:
        print(i)
        break
