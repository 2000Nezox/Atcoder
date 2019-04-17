N = int(input())
a = list(map(int,input().split()))

a.sort()
alice = sum(a[0:N:2])
Bob = sum(a[1:N:2])

result = alice - Bob
result = abs(result)

print(result)
