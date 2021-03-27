class school:
    def fun1(self):
        print("hello")
class student1(school):
    def fun2(self):
        print("hai")
class student2(school):
    def fun3(self):
        print("welcome")
class student3(student1,student2):
    def fun4(self):
        print("thankyou")

obj=student3()
obj.fun4()
obj.fun1()
obj.fun2()
obj.fun3()
