A,B = map(int,input().split())

sum = []
sum.append(A+B)
sum.append(A-B)
sum.append(A*B)

print(max(sum))
