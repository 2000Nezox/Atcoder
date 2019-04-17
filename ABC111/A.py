n = list(input())

for i,data in enumerate(n):
    if data == "1":
        n[i] = "9"
    else:
        n[i] = "1"

print("".join(n))
