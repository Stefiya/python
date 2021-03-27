l=[]
n=int(input("enter a number"))
l.append(n)
def fact(a):
    fact=1
    for i in range(1,n+1):
        fact=fact*i
        i=i+1
    return fact
print(fact(l))