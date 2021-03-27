n=int(input("enter the limit"))
a1=0
a2=1
print(a1,a2,end=" ")
for i in range(0,n):
    c=a1+a2
    print(c,end=" ")
    a1=a2
    a2=c

      