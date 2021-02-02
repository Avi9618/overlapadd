import numpy as np
l=input("Enter the size of x[n] : ")
m=input("Enter the size of h[n] : ")
x=np.zeros(l)
h=np.zeros(m)
print("Enter x[n]")
for i in range(0,l):
    x[i]=input()

print("Enter h[n]")
for i in range(0,m):
    h[i]=input()
bs=input("Enter block size(L) : ")
k=bs+m-1
x1=np.zeros(k)
h1=np.zeros(k)
for i in range(0,m):
    h1[i]=h[i]
x1[0]=1
z=0
y1=np.zeros(k)
b=np.zeros(k)
ch=int(input("1.Overlap add \n2.Exit \n"))
if(ch==1):
    if(l%bs==0):
        g=bs
    else:
        g=bs+1
    Y=np.zeros(l+m-1)
    uk=0
    for i in range(0,g):
        x1=np.zeros(k)
        for j in range(0,bs):
            try:                
                x1[j]=x[j+bs*z]
            except:
                continue
        print x1    
        b[0]=h1[0]
        for j in range(1,k):
            b[j]=h1[k-j]
        for j in range(0,k):
            u=x1*b
            b=np.roll(b,1)
            y1[j]=(np.sum(u))  
        print y1
        z=z+1
        
        if i==0:
            for j in range(0,len(y1)):
                Y[j]=Y[j]+y1[j]
        else:
            uk=uk+bs
            kl=uk
            for j in range(0,len(y1)):
                Y[kl]=Y[kl]+y1[j]
                kl=kl+1
    print("y(n)=")
    print(Y)
    
else:
    print("Thank you")
   

        