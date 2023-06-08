class Employee:
    def __init__(self,empName,empId):
        self.empName=empName;
        self.empId=empId;
        print("In Init")
    def getEmployeeName(self):
        print("Employee Name is Not a Non Employee Name")
    def getEmployee(self,empName):
        print("Enter Employee Name:",self.empName)
    def updateId(self):
        self.empId=12345
        return self.empId;

# Employee.getEmployeeName(emp1)