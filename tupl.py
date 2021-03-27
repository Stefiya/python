l=[]
t1=[]
t2=[]
t=[]
a=int(input("enter range"))
for i in range(0,a):
    b=int(input())
    l.append(b)


t=tuple(l)
p=a//2
t1=tuple(l[0:p])
print(t1)
t2=tuple(l[p:])
print(t2)
