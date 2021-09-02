def calculation(a,left,right,memo,d=0):
    if(a[left:right]==[]):
        return 
    m=max(a[left:right])
    memo[a.index(m)]=d
    b=a.index(m)
    calculation(a,left,b,memo,d+1)
    calculation(a,b+1,right,memo,d+1)
    return
    

for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    memo=[0 for _ in range(n)]
    left=0
    right=n
    calculation(l,left,right,memo)
    print(' '.join(map(str,memo)))