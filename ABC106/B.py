N = int(input())
sum = 0

for i in range(1,N+1,2):
    count = 0
    for x in range(1,N+1):
        if i % x == 0:
            count += 1
    if count == 8:
        sum += 1

print(sum)
