c1_1 = input()
c1_2 = input()
c2_1 = c1_1[::-1]
c2_2 = c1_2[::-1]

if c1_1 == c2_2 and c1_2 == c2_1:
    print("YES")
else:
    print("NO")
