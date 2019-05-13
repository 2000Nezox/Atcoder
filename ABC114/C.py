N = int(input())

def f(s):
    if int(s) > N:                  #ここでNよりも小さいか判定
        return 0                    #超えていた場合は呼び出しをやめる

    ret = 1 if all(s.count(c) > 0 for c in "753") else 0

    for c in "753":
        ret += dfs(s + c)

    return ret

print(f(10))
