from collections import namedtuple
import sys

# syntax -  class collections.namedtuple(typename,filed_names)

# Additional Operations  _fields, _replace()
# declaring nametupe()
Student = namedtuple('Student',['name','age','DOB'])

# Adding values
S = Student('anuja','26','2811995')

# using _fields to display all the keynames of namedtuple()
print ("All the fields of students are : ")
print('_fields: ',S._fields)
print('_field_defaults: ',S._field_defaults)
print()
# using _replace() to change the attribute values of namedtuple
print ("The modified namedtuple is : ")
print(S._replace(name = 'Anu'))
'''
op- All the fields of students are : 
_fields:  ('name', 'age', 'DOB')
_field_defaults:  {}

The modified namedtuple is : 
Student(name='Anu', age='26', DOB='2811995')
'''







sys.exit(0)
# -------------------------------------------------------------------------------------------------------

# COnversion Operations - 1) _make()  2)_asdict()

# declaring nametupe()
Student = namedtuple('Student',['name','age','DOB'])

# Adding values
S = Student('anuja','26','2811995')

# initializing iterable
li = ['shivani','25','331996']

# initiaalizing dict
di = {'name':'priyanka','age':24,'DOB':'441996'}

# using _make() to return namedtuple()
print('The namedtuple instance using iterable is  : ')
print(S._make(li))
print(Student._make(li))
print()
# using _asdict() to return an OrderedDict()
print ("The OrderedDict instance using namedtuple is  : ")
print(S._asdict())
print()
# using ** operator to return namedtuple from dictionary
print ("The namedtuple instance from dict is  : ")
print (Student(**di))

'''
op-The namedtuple instance using iterable is  : 
Student(name='shivani', age='25', DOB='331996')
Student(name='shivani', age='25', DOB='331996')

The OrderedDict instance using namedtuple is  : 
{'name': 'anuja', 'age': '26', 'DOB': '2811995'}

The namedtuple instance from dict is  : 
Student(name='priyanka', age=24, DOB='441996')
'''
# ------------------------------------------------------------------------------------------

# declaring nametuple()

Student = namedtuple('Student',['name','age','DOB'])
S = Student('Anuja','26','2811995')

# access using index
print('The Student age using index is:',S[1])

# access using name
print('The Student name using keyname is:',S.name)

# Access using getattr()
print ("The Student DOB using getattr() is : ",end ="")
print (getattr(S,'DOB'))
'''
op-
The Student age using index is: 26
The Student name using keyname is: Anuja
The Student DOB using getattr() is : 2811995
'''