n=int(input("enter a number"))
for i in range(0,n):
    def rev(n):
        rev=0
        while(n>1):
            rem=n%10
            rev=(rev*10)+rem
            n=n//10
print(rev)
rev(n)