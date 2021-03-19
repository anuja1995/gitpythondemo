from collections import UserDict
import sys

# syntax - class collections.UserDict([initialdata])

d = {'a': 1,
     'b': 2,
     'c': 3}

# Creating an UserDict
userD  = UserDict(d)
print(userD.data)

#  Creating an empty UserDict
userD = UserDict()
print(userD)

sys.exit(0)

# ----------------------------------------------------------------------------------------

# Creating a Dictionary where deletion is not allowed

class MyDict(UserDict):
# Function to stop deleltion
# from dictionary
    def __del__(self):
        raise RuntimeError('Deletion not allowed')

    def pop(self, s=None ):
        raise RuntimeError('Deletion not allowed')

    def popitem(self, s=None):
        raise RuntimeError('Deletion not allowed')

d = MyDict({'a':1,'b':2,'c':3})
d.pop(1)

'''
Traceback (most recent call last):
  File "E:/flask projects/collections/UserDict.py", line 21, in <module>
    d.pop(1)
  File "E:/flask projects/collections/UserDict.py", line 15, in pop
    raise RuntimeError('Deletion not allowed')
RuntimeError: Deletion not allowed
Exception ignored in: <function MyDict.__del__ at 0x0300BF58>
Traceback (most recent call last):
  File "E:/flask projects/collections/UserDict.py", line 12, in __del__
RuntimeError: Deletion not allowed
'''
