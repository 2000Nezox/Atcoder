a,b = map(str,input().split())

if a == "H":
    result = True
else:
    result = False

if (result == True and b == "H") or (result == False and b == "D"):
    print("H")
else:
    print("D")
