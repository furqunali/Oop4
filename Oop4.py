#Abstration Hiding the implementation details of a class only showing the essential features to the usre
#encapsulation wraping data and funtions into a single unit (object)

class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.cluch = False

    def start(self):
       self.cluch = True
       self.acc = True
       print("car start...")

car1 = Car()
car1.start()