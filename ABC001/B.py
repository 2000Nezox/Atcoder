m = int(input())
m = m / 1000
if m <= 0.1:
    print(00)
elif m < 1:
    print('0'+str(m))
elif m <= 5:
    print(m*10)
elif m <= 30:
    print((m+50))
elif