# import sympy
# # print(sum(sympy.divisors(123456789)))
tmp,ans = 1234567890,0
for i in range(1,20000000+1):
    if tmp % i == 0:
        ans = ans + i
print(ans)