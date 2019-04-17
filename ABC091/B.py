N = int(input())
s = []
for i in range(N):
    s.append(input())

M = int(input())
t = []
for i in range(M):
    t.append(input())

money = 0
money_list = []
word_list = list(set(s+t))
for i in range(len(word_list)):
    sum = s.count(word_list[i])
    sum -= t.count(word_list[i])
    if sum < 0:
        sum = 0
    money_list.append(sum)

money_list.sort(reverse = True)
print(money_list[0])
