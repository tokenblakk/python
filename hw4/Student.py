__author__ = 'Tramel Jones'
"""
Student Class, direct comparisons
"""
class Student (object):
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def __eq__(self, other):
        """
        Test for equality
        """
        if self is other:
            return True
        elif type(self) != type(other):
            return False
        else:
            return self.number == other.number and \
                self.name == other.name
            # Check if object is the same student (Name, AND ID No.)

    def __ne__(self, other):
        return not self.__eq__(other)


#   Tested Output
#
# >>> a = Student.Student("Tyler", 17)
# >>> b = Student.Student("Tramel", 44)
# >>> a
# <Student.Student object at 0x02C940F0>
# >>> b
# <Student.Student object at 0x02C94390>
# >>> a==b
# False
# >>> a!=b
# True
# >>> a == a
# True
# >>> b == b
# True
