a=[]
n=int(input("enter limit"))
for i in range(0,n):
        x=int(input("enter elements"));
        a.append(x)
print(a)
large=a[0]
for i in range(0,n):
    if(a[i]>large):
        large=a[i]
print(large)