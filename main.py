class bird:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("My name is",self.name)
        print("My age is",self.age)
    def make_sound(self):
        print("Chirp")


class dog:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def info(self):
        print("My name is",self.name)
        print("My age is",self.age)
    def make_sound(self):
        print("Bark")
obj1=bird("Chucky",5)
obj2=dog("Bingo",7)
for animal in(obj1,obj2):
    animal.info()
    animal.make_sound()