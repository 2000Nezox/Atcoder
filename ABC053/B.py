s = input()

s_first = s.find("A")
s_last = s.rfind("Z")

print(s_last-s_first+1)
