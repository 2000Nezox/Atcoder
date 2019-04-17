X = int(input())

count = []
if X == 1:
    print(1)
else:
    for i in range(1,X):
        for b in range(2,10):
            factorial = i**b
            if factorial <= X:
                count.append(factorial)

    print(max(count))
