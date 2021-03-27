from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class human(animal):
    def move(self):
        print("i can walk")
class snake(animal):
    def move(self):
        print("walk")
class dog(animal):
    def move(self):
        print("i can ")
r=human()
r.move()
k=snake()
k.move()
d=dog()
d.move()
