n = int(input())
a = list(map(int,input().split()))
a.sort()

result = a[-1] - a[0]
print(result)
