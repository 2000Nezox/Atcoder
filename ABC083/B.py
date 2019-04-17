import math
#各桁の和を計算する関数
def findSumOfDigits(n):
    sum = 0
    while n > 0:
        sum += math.floor(n % 10)
        n /= 10

    return sum

N,A,B = map(int,input().split())
total = 0
for a in range(1,N+1):
    sum = findSumOfDigits(a)
    if A <= sum <= B:
        total += a

print(total)
