import  math
N,D = map(int, input().split(' '))
x = [list(map(int,input().split(' '))) for i in range(N)]

result = 0

for i in range(len(x)):

    for i1 in range(i,len(x)):

        tmp1 = x[i]
        tmp2 = x[i1]

        ans = 0
        for i2 in range(len(tmp1)):
            ans = ans + (tmp1[i2]-tmp2[i2])**2
        ans = math.sqrt(ans)

        if ans.is_integer() and 0 < ans:
            result  = result + 1
print(result)


