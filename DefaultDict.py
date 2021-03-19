from collections import defaultdict
import sys

# __missing__()
d = defaultdict(lambda: "Not Present")
d["a"] = 1
d["b"] = 2

print(d.__missing__('a'))
print(d.__missing__('b'))



sys.exit(0)

# ------------------------------------------------------------------------------

# defaultdict(Default_factory)

d = defaultdict(lambda: "Not Present")
d['a'] = 1
d['b'] = 2

print(d['a'])
print(d['b'])
print(d['c'])

# ------------------------------------------------------------------------------

# defaultdict(Default_factory)

def def_value():
    return "Not Present"

d =defaultdict(def_value)
d['a'] = 1
d['b'] = 2

print(d['a'])
print(d['b'])
print(d['c'])

# ---------------------------------------------------------------------------------------------------------

'''
Using List as default_factory
When the list class is passed as the default_factory argument, then a defaultdict is created with the values that are list.
'''

d = defaultdict(list)

for i in range(5):
    d[i].append(i)

print('Dictionary with values as list:')
print(d)

# -------------------------------------------------------------------
'''
 Using int as default_factory
 When the int class is passed as the default_factory argument, then a defaultdict is created with default value as zero.
'''
# Defining the dict
d = defaultdict(int)

L = [1,'a',2,3,4,2,4,1,2]

# Iterate through the list
# for keeping the count
for i in L:
    # The default value is 0
    # so there is no need to enter the key first
    d[i] +=1
print(d)