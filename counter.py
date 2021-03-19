from collections import Counter
import sys

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print(Counter(z))

sys.exit(0)

c1 = Counter(A=4, B=3, C=10)
c2 = Counter(A=10, B=3, C=4)

c1.subtract(c2)
print('c1',c1)
'''
op-
c1 Counter({'C': 6, 'B': 0, 'A': -6})
'''


# ---------------------------------------------------
coun = Counter()
print(coun)

coun.update([1,1,1,1,2,2,2,3])
print(coun)

coun.update([1,2,4])
print(coun)
'''
op:-
Counter()
Counter({1: 4, 2: 3, 3: 1})
Counter({1: 5, 2: 4, 3: 1, 4: 1})
'''

# --------------------------------------------

print("counter With sequence of items: ",Counter(['A','B','A','B','A','B','B','C','B','C']))

print('counter with dictionary: ',Counter({'B':5,'A':3,'C':2}))

print('counter with keyword arguments: ',Counter(A=3,B=5,C=2))