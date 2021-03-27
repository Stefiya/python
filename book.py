class bookstore:
    def __init__(self,b,a):
        self.book=b
        self.author=a
    def book1(self):
        print("book ",self.book)
    def author1(self):
        print("author is",self.author)
ob=bookstore("wings of fire","Dr.A PJ")
ob.book1()
ob.author1()
        

        
        