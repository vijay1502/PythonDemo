class PyCharm:
    def execute(self):
        print("Compile and Run")

class MyCharm:
    def execute(self):
        print("Check,Compile and Run")

class LaptopCoding:
    def code(self,ide):
        ide.execute();
#This concept of polymorphism and method overriding is called duck typing

ide=MyCharm()
lap1=LaptopCoding();
lap1.code(ide)