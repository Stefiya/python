a=int(input("enter 1st number"))
b=int(input("enter 2nd number"))
def swap(a,b):
        temp=a
        a=b
        b=temp
        return a,b
c=swap(a,b)
print(c)
    