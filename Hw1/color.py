__author__ = 'Tramel Jones'
"""
Joins two colors into a brand new super color
"""
_color1 = input("Enter your favorite color: ")
_color2 =input("Enter your second favorite color: ")
cols = [_color1, _color2]
print("Your new favorite color is: " + "-".join(cols) + ".")