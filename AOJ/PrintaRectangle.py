lst = []
while True:
    tmp = list(map(int,input().split()))
    if tmp[0] == tmp[1] == 0:
        break
    else:
        for i in range(tmp[0]):
            print('#'*tmp[1])
        print('')
# for i in lst:
#     if len(lst) == 1:
#         for i1 in range(i[1]):
#             print('#' * i[0])
#         break
#     for i1 in range(i[1]):
#         print('#'*i[0])
#     print()
