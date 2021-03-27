l=[]
n=int(input("enter limit"))
for i in range(0,n):
    x=int(input("enter elements"))
    l.append(x)
print(l)
temp=l[0]
l[0]=l[n-1]
l[n-1]=temp
print(l)