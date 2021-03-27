a=int(input("enter limit"))
l=[]
for i in range (a):
        n=int(input("enter elements"))
        l.append(n)
def add(b):
    sum=0
    for i in b:
        sum=sum+i
    return sum
print(add(l))


