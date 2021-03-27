m=int(input("enter limit"))
n=int(input("enter limit"))
for i in range(m,n+1):
    count=0
    for j in range(2,i//2):
        if(i%j==0):
            count=1
    if(count==1):
        print(i)