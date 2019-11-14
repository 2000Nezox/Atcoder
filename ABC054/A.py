a,b = map(int,input().split())

if a == b:
    print("Draw")
elif a==1 or b == 1:
    if a < b:
        print("Alice")
    else:
        print("Bob")
elif a > b:
    print("Alice")
else:
    print("Bob")
