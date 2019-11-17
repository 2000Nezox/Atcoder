import math
import itertools
N = int(input())
x = [list(map(int,input().split(' '))) for i in range(N)]
length = range(N)
ans = []

for i in itertools.permutations(length): #1,2,3 231

   result = []
   for i1 in range(len(i)-1):
       result.append(math.sqrt((x[i[i1]][0]-x[i[i1+1]][0])**2 + (x[i[i1]][1]-x[i[i1+1]][1]) **2))


   ans.append(sum(result))

print(sum(ans)/len(ans))
