
class Employee:
    emp_count = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.emp_count += 1

    def display_count(self):
        print ("Total Employee %d" % self.emp_count)

    def display_employee(self):
        print ("Name : ", self.name,  ", Salary: ", self.salary)

    def print_emloyee_count(self):
        print("Number of employees")
        return self.emp_count


if __name__ == "__main__" :
    employee1 = Employee("Test1", 1000)
    employee2 = Employee("Test2", 2000)
    employee2.emp_count = 3
    print(employee1.display_count(), employee1.display_employee())
    print(employee2.display_count(), employee2.display_employee())
    print(Employee.emp_count)
