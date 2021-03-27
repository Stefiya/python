str=input("enter a word")
s=" "
for i in str:
    if(i not in "aeiouAEIOU"):
        s=s+i.upper()
    else:
        s=s+i.lower()
print(s)