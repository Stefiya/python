n=int(input("enter a number"))
count=0
for i in range(2,n+1//2):
    if(n%i==0):
        count=1
if(count==0):
    print("it is prime number")
else:
    print("it is not prime number")