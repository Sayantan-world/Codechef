for T in range(int(input())):
    N,X=map(int,input().split())
    A=list(map(int,input().split()))
    totalAmount=sum(A)
    removeMin=totalAmount-min(A)
    if(totalAmount//X != removeMin//X):
        print(totalAmount//X)
    else:
        print(-1)
