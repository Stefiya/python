class parent:
    def first(self):
        print("hello")
class child(parent):
    def second(self):
        print("hai")
object=child()
object.first()
object.second()