str=input("enter a word")
s=" "
l=len(str)
for i in range(l):
    if(i%2==0):
        s=s+str[i].upper()
    else:
        s=s+str[i]
print(s)