class Management:
    #class variables
    typeOfManagement="Engineering";
    def __init__(self,employees,location,category):
        #instance variables
        print("In Management")
        # self.employees=employees
        # self.location=location
        # self.category=category
        #instance variables can be used only with instance methods
    def getEmployees(self): #-->instance method , #accessor method-to get --GETTER METHODs are called accessors as
        # we access values
        return str(self.employees).split("a");
    def functioning(self):
        return "This is fine";

    def setEmployees(self,employeename): #->instance method, #mutator method -to -set -- SETTER Methods are called mutators as
        # we update values
        self.employees=employeename


        #class variables can be used with class methods
    @classmethod #-- decorator(@) must be used for class methods and classmethod
    def information(cls): #-- cls is used for class variables
        return cls.typeOfManagement

        #methods that doesn't want to do with instance or class variables, we use static methods
        #this is useful in operating with other class/module methods
    @staticmethod #-- staticmethod decorator must be used to declare static methods
    def staticEmpl():
        return "This is static nature"

    def visionOfCompany(self):
        print("Doesn't operate in every mode-Management")


class Company(Management):
    def functioning(self):
        print("Operates in every mode!")
    def visionOfCompany(self):
        print("Doesn't operate in every mode-Company")

class CompanyUnderTaker(Company): #Method resolution Order(MRO) will take only insertion order of extending a class
    #for example, CompanyUnderTaker is extending Comapany at beginning, so it will fetch the method from it, if the same
    # method is present in Management class.
    def __init__(self):
        super().functioning()


c1=CompanyUnderTaker();
print(c1.functioning())
