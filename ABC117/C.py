N,M = map(int,input().split())
X = list(map(int,input().split()))
X.sort()
if N >= M: #設置できるコマが座標よりも大きければ終了
    print(0)
    exit()
diff = []
for i in range(1,len(X)):           #座標の差の最大可
    diff.append(X[i]-X[i-1])
diff.sort(reverse=True)
total = sum(diff)
for i in range(N-1):                #移動範囲が広い座標間をショートカット
    total -= diff[i]
print(total)
