l=[]
n=int(input("enter limit"))
odd=[]
even=[]
for i in range(0,n):
    x=int(input("enter elements"))
    l.append(x)
print(l)
for i in range(n):
    if(l[i]%2==0):
        odd.append(l[i])
    else:
        even.append(l[i])
print(odd)
print(even)