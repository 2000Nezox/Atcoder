n = int(input())

for i in range(n,1,-1):
    if (i**(1/2)).is_integer():
        print(i)
        break
else:
    print("1")
