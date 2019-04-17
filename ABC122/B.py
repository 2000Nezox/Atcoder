s = input()

result = []
result_1 = ["A","C","G","T"]
end = False
sum = 0

for i in range(len(s)):
    temporary = i
    sum = 0
    while True:
        if end == True:
            break
        for x in result_1:
            try:
                if s[temporary] == x:
                    sum += 1
                    temporary += 1
                    break
            except:
                end = True
        else:
            result.append(sum)
            break

print(max(result))
