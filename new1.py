class Employee:
    empCount = 0


    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1


    def displayCount(self):
        print('total employee count %d' % Employee.empCount)



    def displayEmployee(self):

        print('Name: ', self.name, 'salary: ', self.salary)

emp1 = Employee('auther', 50000)
emp2 = Employee('ben', 70000)

#hasattr(emp1, 'salary')
#getattr(emp1, 'salary')
#setattr(emp1, 'salary', 90000)

emp1.displayEmployee()
emp2.displayEmployee()
Employee.displayCount(Employee)

print('Employee._doc_:', Employee.__doc__)
print('Employee._dict_:', Employee.__dict__)
print('Employee._name_:', Employee.__name__)
print('Employee._module_:', Employee.__module__)
print('Employee._bases_:', Employee.__bases__)









