lst = [1,0,5]
for i in range(3,35):
    tmp = lst[i-3] + lst[i-2] + lst[i-1]
    lst.append(tmp)
print(lst[31])
print(lst)