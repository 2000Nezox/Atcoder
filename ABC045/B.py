sa = list(input())
sb = list(input())
sc = list(input())
current_order = sa.pop(0)
result = 0
while True:

    if current_order == "a":
        result = sa
    elif current_order == "b":
        result = sb
    elif current_order == "c":
        result = sc

    try:

        current_order = result.pop(0)

    except:
        if current_order == "a":
            print("A")
        elif current_order == "b":
            print("B")
        elif current_order == "c":
            print("C")

        break
