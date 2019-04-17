import math
N = int(input())

result = math.factorial(N)

print(result%(10**9+7))
