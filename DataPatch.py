class doIt:


    def __init__(self,name):
        self.name=name;


    def checkCond(self):
        if str(self.name).__contains__("Vi"):
            yield "Vi",self.name,10

        else:
            return None
    def looper(self):
        num = 1;
        while num<=10:

            sq=num*num
            yield sq
            num+=1

di=doIt("Vijaya");
print(di.checkCond().__next__())
for i in di.looper():
    print(i)