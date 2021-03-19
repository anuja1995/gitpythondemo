from collections import UserList
import sys

# syntax- class collections.UserList([list])

# Creating a List where deletion is not allowed
class MyList(UserList):
    # Function to stop deleltion from List
    def remove(self, s=None):
        raise RuntimeError('Deletion not allowed')

    # Function to stop pop from List
    def pop(self, s=None):
        raise RuntimeError('Deletion not allowed')

# Driver's code
L = MyList([1,2,3,4])

print('Original list: ',L)

# Inserting to List"
L.append(5)
print("After Insertion")
print(L)
print()
# Deliting From List
L.remove()

'''
op-
Original list:  [1, 2, 3, 4]
After Insertion
[1, 2, 3, 4, 5]

Traceback (most recent call last):
  File "E:/flask projects/collections/UserList.py", line 27, in <module>
    L.remove()
  File "E:/flask projects/collections/UserList.py", line 10, in remove
    raise RuntimeError('Deletion not allowed')
RuntimeError: Deletion not allowed

'''