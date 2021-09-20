a,b=map(int,input().split())
l=[b]
while a<b:
    if b%2:
        b-=1
        if b%10==0:b//=10
        else:exit(print("NO"))
    else:b//=2
    l+=[b]
if b<a:print("NO")
else:print("YES\n",len(l),"\n",*l[::-1])