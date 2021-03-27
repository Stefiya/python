class person:
    def __init__(self,name,age):
        self.n=name
        self.a=age
    def my_function(self):
        print("my name is",self.n)
p=person("john",36)
p.my_function()

class car:
    def __init__(self,m,col,s):
        self.model=m
        self.color=col
        self.speed=s
maruthy=car(800,"red",180)
print(maruthy.model)
print(maruthy.color)
print(maruthy.speed)

benz=car(102,"blue",190)
print(benz.model)
print(benz.color)
print(benz.speed)
        