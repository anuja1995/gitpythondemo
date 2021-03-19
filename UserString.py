from collections import UserString
import sys

# syntax - class collections.UserString(seq)


# Creating a Mutable String
class MyString(UserString):
    # Function to append to string
    def append(self,s):
        self.data += s

    # Function to rmeove from string
    def remove(self,s):
        self.data = self.data.replace(s,"")

# Driver's code
s1 = MyString('Geeks')
print('Original String:',s1)

# Appending to string
s1.append("s")
print("String After Appending:",s1)

# Removing from string
s1.remove("e")
print("String after Removing:",s1)

'''
op-Original String: Geeks
String After Appending: Geekss
String after Removing: Gkss
'''

sys.exit(0)

# ---------------------------------------------------------------------------------

d = 12344

# Creating an UserString
userD = UserString(d)
print(userD)

# Creating an empty UserString
userD = UserString("")
print(userD)

'''
op- 12344
'''