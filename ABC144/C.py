import math
N = int(input())

for i in range(int(math.sqrt(N))+1,0,-1):
    if N%i == 0:
        j = N//i
        print(j+i-2)
        break

