import re
A,B = input().split(' ')
if len(A) == 1 and len(B) == 1:
    print(int(A)*int(B))
else:
    print(-1)