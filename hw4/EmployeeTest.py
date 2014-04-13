__author__ = 'Tramel Jones'

import Employee
e = Employee.Employee("Steve Jobs", 700051364)
f = Employee.Employee("Mark Jacobs", 2334512)
g = Employee.Employee("Carl", 14982)

employees = [e,f,g]
print(employees.__str__())
for emp in employees:
    print(emp.__str__())
