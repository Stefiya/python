class parent:
    def fun1(self):
        print("hello")
class child1(parent):
    def fun2(self):
        print("hai")
class child2(child1):
    def fun3(self):
        print("welcome")
ob=child2()
ob.fun1()
ob.fun2()
ob.fun3()
