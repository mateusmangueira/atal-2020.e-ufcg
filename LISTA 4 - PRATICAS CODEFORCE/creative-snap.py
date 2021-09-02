(p,k,A,B) = [int(e) for e in input().split()]
K = tuple([int(e) for e in input().split()])
 
d = {}
 
def function(p,K,A,B):
    if p == 0:
        if len(K) == 0:
            return A
            
        else:
            
            return B*len(K)
 
    if len(K) != 0:
        op1 = B*len(K)*2**p
    else:
        op1 = A
    ref = (2**p)//2
    Kl = tuple([e for e in K if e <= ref])
    Kr = tuple([e-ref for e in K if e > ref])
    if (p,Kl) in d:
        LL = d[(p,Kl)]
    else:
        tmp = function(p-1,Kl,A,B)
        d[(p,Kl)] = tmp
        LL = tmp
    if (p,Kr) in d:
        RR = d[(p,Kr)]
    else:
        tmp = function(p-1,Kr,A,B)
        d[(p,Kr)] = tmp
        RR = tmp
    op2 = LL+RR
    return min(op1, op2)
 
print(function(p,K,A,B))