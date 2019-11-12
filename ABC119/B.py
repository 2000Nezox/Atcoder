def func1(lst, value): return [i for i, x in enumerate(lst) if x == value]
def func2(coping, lst, coefficient=1):return sum(lst[i] * coefficient for i in coping)
lst = [input().split(' ') for i in range(int(input()))]
X = [float(i[0]) for i in lst]
Y = [i[1] for i in lst]
print(func2(func1(Y,"BTC"),X,380000.0) + func2(func1(Y,"JPY"),X))