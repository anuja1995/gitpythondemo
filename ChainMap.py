from collections import ChainMap
import sys
# syntax - class collections.ChainMap(dict1, dict2)


# Manipulating Operations--1)new_child(),  2)reversed()

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'b' : 3, 'c' : 4 }
dict3 = { 'f' : 5 }

chain = ChainMap(dict1,dict2)
print ("All the ChainMap contents are : ")
print (chain.maps)

# using new_child() to add new dictionary
chain1 = chain.new_child(dict3)

print ("Displaying new ChainMap : ")
print (chain1.maps)

print ("Value associated with b before reversing is : ",end="")
print (chain1['b'])

# reversing the ChainMap
chain1.maps = reversed(chain1.maps)
print ("Value associated with b after reversing is : ",end="")
print (chain1['b'])
'''
op-
All the ChainMap contents are : 
[{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
Displaying new ChainMap : 
[{'f': 5}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
Value associated with b before reversing is : 2
Value associated with b after reversing is : 3
'''

sys.exit(0)


# -------------------------------------------------------------------------------------

# Let’s see various Operations on ChainMap--

# Access Operations---1)keys(),  2)values(),  3)maps()

dict1 = { 'a' : 1, 'b' : 2 }
dict2 = { 'b' : 3, 'c' : 4 }

chain = ChainMap(dict1,dict2)

print ("All the ChainMap contents are : ")
print (chain.maps)

print ("All keys of ChainMap are : ")
print (list(chain.keys()))

print ("All values of ChainMap are : ")
print (list(chain.values()))
'''
op-
All the ChainMap contents are : 
[{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]
All keys of ChainMap are : 
['b', 'c', 'a']
All values of ChainMap are : 
[2, 4, 1]

'''

# ---------------------------------------------------------------

# Adding new dictionary -A new dictionary can be added by using the new_child() method.
# The newly added dictionary is added at the beginning of the ChainMap.

dic1 = { 'a' : 1, 'b' : 2 }
dic2 = { 'b' : 3, 'c' : 4 }
dic3 = { 'f' : 5 }

chain = ChainMap(dic1,dic2)
print ("All the ChainMap contents are : ")
print(chain)

# using new_child() to add new dictionary
chain1 = chain.new_child(dic3)

print ("Displaying new ChainMap : ")
print(chain1)

'''
op-
 All the ChainMap contents are : 
ChainMap({'a': 1, 'b': 2}, {'b': 3, 'c': 4})
Displaying new ChainMap : 
ChainMap({'f': 5}, {'a': 1, 'b': 2}, {'b': 3, 'c': 4})
'''

# ---------------------------------------------------------------

# Accessing Keys and Values from ChainMap

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

c = ChainMap(d1,d2,d3)

# Accessiing values using name
print('Accessiing values using name a: ',c['a'])

# Accessing value using Values
print('Accessing value using Values ',c.values())

# Accessing keys using keys
print('Accessing keys using keys:',c.keys())

'''
op-
Accessiing values using name a:  1
Accessing value using Values  ValuesView(ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}))
Accessing keys using keys: KeysView(ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}))
'''


# ---------------------------------------------------------------

d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d3 = {'e': 5, 'f': 6}

# defining chainmap

cm = ChainMap(d1,d2,d3)
print(cm)
'''
op- ChainMap({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6})
'''
