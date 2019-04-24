N = int(input())
h = list(map(int,input().split()))
h_set = list(set(h))

old = 0

def f(k,old):
    count_k = 0

    if not k:
        return 0
    elif len(k) == 1:
        return 1
    elif len(k) == 2:
        return 2

    #print(k)

    k_index = k.index(min(k))
    count_k += min(k) - old
    old = min(k)

    #print(k_index,count_k,old)

    k.pop(k_index)
    print(k,k[:k_index],k[k_index:])
    count_k += f(k[:k_index],old)
    count_k += f(k[k_index:],old)
    return count_k


print(f(h,0))
print(f(h_set,0))
