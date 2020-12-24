lst = list(map(str,input().split()))
lst = [str.swapcase(i) for i in lst]
print(' '.join(lst))