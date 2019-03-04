T=int(input())
for t in range(T):
    s=input().split()
    N=int(s[0])
    K=int(s[1])
    number=[]
    
    for i in range(1,N+1):
        number.append(i)
    if K==0:
        print (' '.join(str(e) for e in number))
    else:
        if N % (2*K)==0:
            for j in range(0,int(N/(2*K))):
                for i in range(1,K+1):
                    temp=number[j*2*K+i-1]
                    number[j*2*K+i-1]=number[j*2*K+i+K-1]
                    number[j*2*K+i+K-1]=temp
            print (' '.join(str(e) for e in number))
        else:
            print (-1)
