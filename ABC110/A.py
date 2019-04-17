sequence = list(map(int,input().split()))

sequence.sort(reverse = True)
A = str(sequence.pop(0))
A += str(sequence.pop(0))
B = sequence.pop(0)
C = int(A) + B
print(C)
