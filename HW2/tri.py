__author__ = 'Tramel Jones'
"""
Program that takes 3 inputs and returns whether triangle is equilateral
"""

s = []
for i in range(1,4):
    s.append(input("Side %d?" %i))
print(s)

if s[0]==s[1]==s[2]:
    print ("Equilateral Triangle")
else:
    print ("Not a valid equilateral Triangle.")