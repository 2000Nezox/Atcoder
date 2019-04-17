abc_list = list(map(int,input().split()))
K = int(input())

for k in range(K):
    abc_list.sort(reverse = True)
    abc_list[0] = abc_list[0] * 2

print(sum(abc_list))
