A,B = map(int,input().split())

sum = A + B -1
land_area = A * B
land_area -= sum
print(land_area)
