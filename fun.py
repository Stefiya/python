#def my_function():
    #print("hello")
#my_function()
#def my_function(fname):
    #print(fname)
#my_function("email")
#def my_function(fname):
    #print(fname+"hello")
#my_function("email")
#my_function("mobile")
#my_function("orisys")
def my_function(* name):
    print(name)
my_function("email","mobile")
def my_function(* kids):
    print("the youngest child is "+kids[2])
my_function("ammu","achu","arya")
def my_function(name1,name2,name3):
    print(name2)
my_function(name3="ammu",
            name1="achu",
            name2="arya")
def my_function(country="india"):
    print("i am from "+country)
my_function("canada")
my_function()
my_function("america")
def my_function(x):
    return 5*x
print(my_function(3))
print(my_function(5))
print(my_function(10))
def my_function(x):
    str="python"
    x=20
    return str,x
str,x=my_function()
print(str)
print(x)

