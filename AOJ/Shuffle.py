while True:
    ans = input()
    if ans == '-':
        break
    m = int(input())
    for i in range(m):
        x = int(input())
        ans = ans[x:] + ans[:x]
    print(ans)
