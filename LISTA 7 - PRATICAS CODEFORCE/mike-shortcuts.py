n = int(input())
a = list(map(int,input().split()))
 
d = [-1] * n
d[0] = 0
p = [0]
 
for i in p:
  for j in [i - 1, i + 1, a[i] - 1]:
    if j >= 0 and j < n and d[j] == -1:
      d[j] = d[i] + 1
      p.append(j)
 
print(*d)