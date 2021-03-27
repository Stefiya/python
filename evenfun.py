def even(a):
    e=[]
    for i in a:
        if(i%2==0):
            e.append(i)
    return e


l=[]
n=int(input("enter limit"))
for i in range(0,n):
    x=int(input("enter elements"))
    l.append(x)
print(l)
print(even((l)))
