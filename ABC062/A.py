x,y = map(int,input().split())

list1 = {1,3,5,7,8,10,12}
list2 = {4,6,9,11}
list3 = {2}
result = "No"

set_list = [list1,list2,list3]
for data in set_list:
    if x in data:
        if y in data:
            result = "Yes"

print(result)
