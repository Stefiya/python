n=int(input("enter limit : "))
for i in range(1,n+1):
    print("Multiplication Table of ",i)
    for j in range(1,11):
        k=i*j
        print("{} * {} ={}".format(j,i,k)) 
