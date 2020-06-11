tmp,count = 0,0,
for i in range(600,0,-1):
    tmp = tmp + i
    if tmp > 5000:
        tmp = i
        count = count + 1
else:
    if tmp != 0:
        count = count + 1
print(count)

