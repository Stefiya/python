l=[]
n=int(input("enter limit"))
for i in range(0,n):
    x=int(input("enter elements"))
    l.append(x)
print(l)
l.insert(5,"hai")
print(l)
if(33 in l):
    l.remove(33)
else:
    print("not found")
print(l)