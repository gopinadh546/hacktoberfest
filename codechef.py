import math
a=[]
t=int(input())
for i in range(t):
    x=0
    n,k=map(int,input().split())
    b=list(map(int,input().split()))
    count=0
    """
    if(n==1):
        i=0
        while(b[i]>=k):
            h=b[i]-k
            b[i]=b[i]-k
            count+=1
            if(b[i]<k):
                x=count+1
                break;
    
    else:
        s=sum(b)
        d=math.floor(s/k)
        v=s%k
        v=v/k
        x=math.ceil(d+v)
    """
    count=0 
    c=0
    if(n==1):
        i=0
        while(b[i]>=k):
            h=b[i]-k
            b[i]=b[i]-k
            count+=1
            if(b[i]<k):
                x=count+1
                break;
    else:           
        i=0 
        while(i<n-1):
            if(b[i]>=k):
                h=b[i]-k
                b[i]=0
                count+=1
                b[i+1]+=h
            if(b[i+1]<k):
                x=count+1
                break
            if(b[i+1]>=k and i==n-2):  
                h=b[i+1]-k
                b[i+1]=0
                count+=1
                b[0]+=h
                if(b[0]<k):
                    x=count
                    break
                i=0;
                continue
            i+=1                        
    
    a.append(x)                        
for i in a:
    print(i)
"""
def pth(a,p,N):
    if(N==2):
        if p==1:
            pt=min(c)
            e=index(pt)
        elif(p==2):
            a.sort()
            pt=a[0]
            e=0
    elif(N==1):
        t=a[0]
        e=0
    else:
        a.sort()
        kt=c[p-1]
        e=p-1
    return e
b=[]
y=int(input())
for i in range(y):
    j=0
    c=[]
    v=0
    count=0
    count1=0
    N,X,p,k=map(int,input().split())
    a=list(map(int,input().split()))
    for i in a:
        c.append(i)
    if(N==2):
        if k==1:
            kt=min(c)
            e=index(kt)
        elif(k==2):
            c.sort()
            kt=c[0]
            e=0
    elif(N==1):
        kt=a[0]
        e=0
    else:
        c.sort()
        kt=c[k-1]
        e=k-1
    for i in a:
        if X not in a:
            v=-1
            break
    if(v==-1):
        count=v
    else:
        for i in range(len(a)):        
            a.sort()
            d=a[e]
            a[e]=a[i]
            f=pth(a,p,N)
            if(a[f]==X):
                count+=1
                break
            else:
                a[i]=d
                continue   
    b.append(count)
for i in range(len(b)):
    print(b[i])    
"""
