A,B,X = map(int,input().split())

left = 0
right = 10**9+1
n = 10**5

while right - left > 1:
    d = len(str(n))
    price = A * n + B * d
    if price > X:
        right = n
    else:
        left = n
    n = (right + left) // 2

print(n)


