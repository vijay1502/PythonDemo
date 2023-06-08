import CALCULATOR
from abc import ABC,abstractmethod
import GenderCategory
class CALLER:
    # Method Overloading
    def sum(self,a=None,b=None,c=None):
        if a!=None and b!=None and c!=None:
            return a+b+c;
        elif a!=None and b!=None:
            return a+b;
        else:
            return a;

class RINGER(CALLER):
    pass

# print(__name__)
    if __name__=="__main__":
        print("Vijaya Kanugovi")
        print(CALCULATOR.mul(2,3))


class AbstractReason:
    def reasonForQuit(self):
        pass

class getEmployeeReason(AbstractReason):
    @abstractmethod
    def reasonForQuit(self):
        print("SELF REALIZATION")


c=RINGER;
print(c.sum(2,3,9));

gemp=AbstractReason();
gemp.reasonForQuit()