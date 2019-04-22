N = int(input())
h = list(map(int,input().split()))
count = 0
temporary = 0
def f(h):
    if h.count(0) == len(h):
        return 0

    h_min = min(h)
    new_h = [c-h_min for c in h ]
    h_min += f(new_h[1:])

    return h_min

try:
    for i in range(len(h)):
        h.remove(0)
except:
    pass

print(h)
h_min = min(h)
count = h_min
new_h = [c-h_min for c in h]
for i in range(len(new_h)):
    if new_h[i] == 0:
        count += f(new_h[temporary:i])
        temporary = i
        print(count,)



print(count)
