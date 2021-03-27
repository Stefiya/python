class rectangle:
    def __init__(self,l,br):
        self.l=l
        self.b=br
    def get_area(self):
        area=self.l*self.b
        print("area is",area)
        
    def get_perimeter(self):
        perimeter=2*(self.l+self.b)
        print("pm is",perimeter)
       
r=rectangle(3,4)
r.get_area()
r.get_perimeter()

        