input()
inf=1<<9
S=0,0,0
for a in map(int,input().split()):S=1+min(S),min(S[0],S[2])if a>>1 else inf,min(S[0],S[1])if 1&a else inf
print(min(S))