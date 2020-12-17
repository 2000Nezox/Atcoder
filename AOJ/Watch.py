S = int(input())
h, S = divmod(S, 3600)
m, S = divmod(S, 60)
print('{}:{}:{}'.format(h, m, S))
