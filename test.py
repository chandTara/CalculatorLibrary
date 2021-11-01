
class Employee:
   empCount = 0

   def __init__(self, name, salary):
       self.name = name
       self.salary = salary
       Employee.empCount += 1

   def displayCount(self):
       print ("Total Employee %d" % self.empCount)

   def displayEmployee(self):
       print ("Name : ", self.name,  ", Salary: ", self.salary)

   def printEmloyeeCount(self):
       print("Number of employees")
       return self.empCount


if __name__ == "__main__" :
    employee1 = Employee("Test1", 1000)
    employee2 = Employee("Test2", 2000)
    employee2.empCount = 3
    print(employee1.displayCount(), employee1.displayEmployee())
    print(employee2.displayCount(), employee2.displayEmployee())
    print(Employee.empCount)
