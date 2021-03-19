from collections import deque
import sys

# syntax - class collections.deque(list)

# other functions-- 1)extend(iterable), 2)extendleft(iterable), 3)reverse(), 4)rotate()
# initializing deque
de = deque([1,2,3])
print(de)

# using extend() to add numbers to right end
# adds 4,5,6 to right end
de.extend([4,5,6])

# printing modified deque
print ("The deque after extending deque at end is : ")
print(de)

# using extendleft() to add numbers to left end
# adds 7,8,9 to right end
de.extendleft([7,8,9])

# printing modified deque
print ("The deque after extending deque at beginning is : ")
print(de)

# using rotate() to rotate the deque
# rotates by 3 to left
de.rotate(-3)

# printing modified deque
print ("The deque after rotating deque is : ")
print(de)

# using reverse() to reverse the deque
de.reverse()

# printing modified deque
print ("The deque after reversing deque is : ")
print(de)

'''
op- deque([1, 2, 3])
The deque after extending deque at end is : 
deque([1, 2, 3, 4, 5, 6])
The deque after extending deque at beginning is : 
deque([9, 8, 7, 1, 2, 3, 4, 5, 6])
The deque after rotating deque is : 
deque([1, 2, 3, 4, 5, 6, 9, 8, 7])
The deque after reversing deque is : 
deque([7, 8, 9, 6, 5, 4, 3, 2, 1])
'''

sys.exit(0)
# -------------------------------------------------------------------------------------------

# other functions-- 1)index(ele, beg, end), 2)insert(i, a), 3)remove(), 4)count()

# initializing deque
de = deque([1,2,3,3,4,2,4])
print(de)

# using index() to print the first occurrence of 4
print ("The number 4 first occurs at a position : ")
print(de.index(4,2,5))

# using insert() to insert the value 3 at 5th position
de.insert(4,3)

# printing modified deque
print ("The deque after inserting 3 at 5th position is : ")
print(de)

# using count() to count the occurrences of 3
print ("The count of 3 in deque is : ")
print(de.count(3))

# using remove() to remove the first occurrence of 3
de.remove(3)

# printing modified deque
print ("The deque after deleting first occurrence of 3 is : ")
print(de)

'''
op-deque([1, 2, 3, 3, 4, 2, 4])
The number 4 first occurs at a position : 
4
The deque after inserting 3 at 5th position is : 
deque([1, 2, 3, 3, 3, 4, 2, 4])
The count of 3 in deque is : 
3
The deque after deleting first occurrence of 3 is : 
deque([1, 2, 3, 3, 4, 2, 4])
 
'''

# -------------------------------------------------------------------------------------------

# Removing Elements - pop(), popleft()
de = deque([6,1,2,3,4])
print(de)

# using pop() to delete element from right end
# deletes 4 from the right end of deque
de.pop()

# printing modified deque
print ("The deque after deleting from right is : ")
print(de)

# using popleft() to delete element from left end
# deletes 6 from the left end of deque
de.popleft()

# printing modified deque
print ("The deque after deleting from left is : ")
print(de)

'''
op- deque([6, 1, 2, 3, 4])
The deque after deleting from right is : 
deque([6, 1, 2, 3])
The deque after deleting from left is : 
deque([1, 2, 3])
'''
# -------------------------------------------------------------------------------------------

# Inserting arguments --> append(),appendleft()

# initializing deque
de = deque([1,2,3])

# using append() to insert element at right end
# inserts 4 at the end of deque
de.append(4)

# printing modified deque
print ("The deque after appending at right is : ")
print(de)

# using appendleft() to insert element at right end
# inserts 6 at the beginning of deque
de.appendleft(6)

# printing modified deque
print ("The deque after appending at left is : ")
print(de)

'''
op-The deque after appending at right is : 
deque([1, 2, 3, 4])
The deque after appending at left is : 
deque([6, 1, 2, 3, 4])
'''

# ----------------------------------------------------------------------

# Declaring deque
dq = deque(['name','age','DOB'])
print(dq)

'''
op- deque(['name', 'age', 'DOB'])
'''


