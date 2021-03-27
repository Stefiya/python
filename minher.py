class parent1:
    def fun1(self):
        print("hello")
class parent2:
    def fun2(self):
        print("hai")
class child(parent1,parent2):
    def fun3(self):
        print("welcome")
ob=child()
ob.fun1()
ob.fun2()
ob.fun3()