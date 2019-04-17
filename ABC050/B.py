n = int(input())
t = list(map(int,input().split()))
m = int(input())

list = []
for i in range(m):
    p,x = map(int,input().split())
    new_list = t.copy()
    new_list[p-1] = x
    list.append(sum(new_list))

for i in list:
    print(i)
