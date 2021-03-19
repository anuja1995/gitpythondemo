from collections import OrderedDict
import sys

print('---Before Deleting-----')
od = OrderedDict()
print(od)
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key,value in od.items():
    print(key,value)


print('---After Deleting-----')
od.pop('a')
for key,value in od.items():
    print(key,value)

print('---After Re-inserting key value-----')

od['a'] = 11
for key,value in od.items():
    print(key,value)


sys.exit(0)

# Key value Change

print('---Before Updating value-----')
od = OrderedDict()
print(od)
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key,value in od.items():
    print(key,value)

od['c'] = 55

print('---After Updating value for key c-----')
for key,value in od.items():
    print(key,value)


# ---------------------------------------------------------------------------------------------

# Deletion and Re-Inserting

print('---Before Deleting-----')
od = OrderedDict()
print(od)
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key,value in od.items():
    print(key,value)

od.pop('a')

# re-inserting 'a'
od['a']=1

print('------After Re-inserting----')
for key,value in od.items():
    print(key,value)

# ------------------------------------------------------------------------------------

print('Normal dictionary')
d = {}
print(d)
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key,value in  d.items():
    print(key,value)

print('OrderDict')
od = OrderedDict()
print(od)
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key,value in od.items():
    print(key,value)

# --------------------------------------------------------------------

roll_no =OrderedDict([
    (11,'Anuja'),
    (9,'shivani'),
    (17,'priyanka')
])
print(type(roll_no))
for key,value in roll_no.items():
    print(key, value)
