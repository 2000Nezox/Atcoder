taro, hana = 0, 0
n = int(input())
for i in range(n):
    lst = list(input().split())
    tmp = lst[0]
    lst.sort()
    if lst[0] == lst[1]:
        taro = taro + 1
        hana = hana + 1
    elif lst[0] == tmp:
        hana = hana + 3
    else:
        taro = taro + 3
print(taro, hana)
