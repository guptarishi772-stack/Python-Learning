class Animals:
    pass

class Cats(Animals):
    pass

class Dog(Cats):
    @staticmethod
    def bark():
        print("bow Bow!!")

D  = Dog()
D.bark()        