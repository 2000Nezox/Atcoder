X = input()
A = input()
B = input()

X,A,B = int(X),int(A),int(B)
X -= A
X %= B

print(X)
