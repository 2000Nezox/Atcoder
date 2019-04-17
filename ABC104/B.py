s = input()

ans = "WA"
if s[0] == "A" and s[2:-1].count("C") == 1 and s[1] != "C" and s[-1] != "C":
    s2 = s.replace("A","a").replace("C","c")
    if s2 == s.lower():
        ans = "AC"

print(ans)
