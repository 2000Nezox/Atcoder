lst = [0] * 26
while True:
    try:
        x = str.lower(input())
        for i in range(97, 123):
            lst[i - 97] = x.count(chr(i)) + lst[i - 97]
    except EOFError:
        break

lst = [str(i) for i in lst]
for i in range(97, 123):
    print(chr(i) + ' : ' + lst[i - 97])
