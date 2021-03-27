l=[1,2,3,4,5]
print(l)
n=len(l)
temp=l[0]
l[0]=l[n-1]
l[n-1]=temp
print(l)