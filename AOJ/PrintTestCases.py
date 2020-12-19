lst = []
while True:
    x = int(input())
    if x != 0:
        lst.append(x)
    else:
        break

for i, number in enumerate(lst):
    print("Case {}: {}".format(i+1, number))
