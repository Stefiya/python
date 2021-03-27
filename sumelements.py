l=[]
sum=0
n=int(input("enter limit"))
for i in range(0,n):
    x=int(input("enter elements"))
    l.append(x)
print(l)
for i in range(0,n):
    sum=sum+l[i]
print(sum);