n=int(input("enter a number"))
total=0
x=n
while(x!=0):
    rem=x%10
    total=total+rem*rem*rem
    x=x//10
if(n==total):
    print("it is armstrong number")
else:
    print("it is not armstrong number")