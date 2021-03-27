class father:
    def transportation(self):
        print("cycle")
class son(father):
    def transportation(self):
        print("bike")
obj=son()
obj.transportation()