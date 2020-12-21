n = int(input())
a = list(map(int,input().split()))
a = a[::-1]
a = [str(i) for i in a]
print(' '.join(a))