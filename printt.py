n=int(input("enter a  number"))
for i in range(0,n):
    for j in range(0,n):
        if(i==0 or j==0 or j==n-1 or i==n-1 or i==n/2 or j==n/2):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print(" ")
      
          
          

        