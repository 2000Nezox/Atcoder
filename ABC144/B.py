N = int(input())
for i in range(1,10):
    for i1 in range(1,10):
        if (i*i1) == N:
            print("Yes")
            exit()
print("No")