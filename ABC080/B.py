N = input()
lst = [int(N[i]) for i in range(len(N))]

if (int(N) % sum(lst)) == 0:
    print("Yes")
else:
    print("No")