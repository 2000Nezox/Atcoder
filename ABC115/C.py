N,K = map(int,input().split())
tree_list,new_tree_list = [],[]
for i in range(N):
    tree_list.append(int(input()))

tree_list.sort(reverse=True)

for i in range(len(tree_list)-K+1):
    new_tree_list.append(tree_list[0+i]-tree_list[K+i-1])
new_tree_list.sort()
print(new_tree_list[0])
