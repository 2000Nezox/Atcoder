    a,b = map(str, input().split())
    a += b
    c = 1
    result = 0
    while(True):
        result = c*c
        if result > int(a):
            print("No")
            break
        elif result == int(a):
            print("Yes")
            break

        c += 1
