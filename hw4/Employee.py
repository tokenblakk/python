__author__ = 'Tramel Jones'
"""
Employee Class
"""
class Employee:
    def __init__(self, name, sal):
         self.name = name
         self.salary = sal

    def salary(self):
        return self.salary
    def getName(self):
        return self.name
    def __str__(self):
        return "Employee Name: \n" + self.getName() + "\n Annual Salary:\n$" + str(self.salary) + "\n"