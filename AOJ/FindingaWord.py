count = 0
w = input()
while True:
    tmp = list(input().split())

    if 'END_OF_TEXT' in tmp:
        break
    for i in tmp:
        x = str.lower(i)
        if x == w:
            count = count + 1
print(count)
