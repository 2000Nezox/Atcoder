lst = []
while True:
    tmp = input()
    tmp1 = list(map(str,tmp.split()))
    if "?" in tmp1:
        break
    else:
        lst.append(tmp)

for i in lst:
    x = eval(i)
    print(int(x))

