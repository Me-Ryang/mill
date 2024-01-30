H,M=map(int,input().split())

if(M>=45):
    print(H,M-45)
elif(M<45):
    M+=15
    if(H==0):
        print(23,M)
    else:
        H-=1    
        print(H,M)