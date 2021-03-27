class parent:
    def fun1(self):
        print("hello")
class child1(parent):
    def fun2(self):
        print("hai")
class child2(parent):
    def fun3(self):
        print("welcome")
obj=child1()
ob=child2()
ob.fun1()
obj.fun2()
ob.fun3()
obj.fun1()
        