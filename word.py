a=str(input("enter string"))
arr=a.split()
s=" "
count=0
for i in range(len(arr)):
    s=arr[i]
    if(s[0]=='a' or s[0]=='A'):
        count+=1
print(count)