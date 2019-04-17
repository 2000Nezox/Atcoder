N = int(input())

sum = 0
count = 1
while True:
    sum = N * count
    if sum % 2 == 0 and sum % N == 0:
        print(sum)
        break
    count += 1
