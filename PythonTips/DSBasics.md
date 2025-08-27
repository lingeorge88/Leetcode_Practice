# Python Tips for Coding Interviews


## Variable Assignments
```python
x, y, z = 0, 'a', True  #multiple assignments
x++ # invalid
x += 1 # valid
None # null type
```

## Math
```python
5 / 2 #decimal by default
5 //2 # use double slash to round down

3 // 2 # 2 -> Does not round toward 0 by default
int(3/2)  # rounds towards 0

10 % 3 # -> 1
-10 % 3 # -> 2

# to be consistent with other languages:
import math
math.fmod(-10, 3)

# common math functions
math.pow(3, 3)
math.sqrt(9)
math.ceil(3 / 2)
math.floor(3 / 2)

# infinity
float("inf")
float("-inf")
```

## Lists
```python
arr = [1,2,3]
arr.append(4) # adds element to the end
arr.pop() # removes element from the end
arr.insert(1, 7) # inserts element at postion 1

arr2 = [1] * n # initialize array of size n with default value of 1
arr2[-1], arr[-2] # last value, second to last value, etc

# sublists/slicing
arr3 = [8,9,88,99,77]
arr3[1:3] # [9,88], last index is noninclusive

# unpacking
a, b, c = [1, 2, 3] # must be same # of variables as elements

# iterate with index and value
for i, n in enumerate(arr):
	print(i, n) #-> 0, 1  1, 2, 2, 3

# loop through multiple lists simultaneously while unpacking
arr1 = [1,2,3]
arr2 = [4,5,6]
for n1, n2 in zip(arr1, arr2):
	print(n1, n2) # -> 1 4, 2 5, 3, 6
# reverse a list
arr1.reverse()

# sorting
arr1.sort() # modified list in place
sorted(arr1) # creates a copy of sorted list
# reverse sorting logic
arr1.sort(reverse = True)

# custom sort (default sorts by alphabetical order)
names = ['bob', 'alice', 'jones']
names.sort(key = lambda x:len(x))
```
### List Comprehension
```python
arr = [ i for i in range(6)] # [0, 1, 2, 3, 4, 5]

# 2-D lists
arr2d = [ [0] * 3 for i in range(3)] 
# [[0,0,0] , [0,0,0], [0,0,0]]
```
## Strings
```python
# strings are immutable, so when we modify a string we create a new copy
str1 = 'abc'
str1 += 'd' # creates a new string

# can be sliced like lists
str1[1:2] #'b'

# can be converted to ints and backwards
int('123') + int('123') #246
str(123) + str(123) # '123123'

# ascii value of a char
ord('a') # 97
ord('b') # 98

# combine a list of strings (with empty character as delimiter)
strs = ['ab', 'cd', 'ef']
"".join(strs) # 'abcdef'
```



## Queues / Deque
```python
from collections import deque

queue = deque()
queue.append(1)
queue.append(2)

queue.popleft() # pop from left
queue.appendleft() # add to left
queue.pop() # pop from right
```

## Hashset
```python
#initialize a set
hashset = set()

# adding elements
hashset.add(1)
hashset.add(2)

# removing elements
hashset.remove(2)

# check memebership 
1 in hashset

# check size
len(hashset)

# set comprehension
myset = {i for i in range(5)}

# list to set 
set([1,2,3])


```
## Hashmaps / Dict
```python
myMap = {}
myMap['alice'] = 88
myMap['bob'] = 77

print(len(myMap)) # 2

# check membership
print("alice" in myMap)

# remove a value by key
myMap.pop("alice")

# dict comprehension
myMap = {i: 2*i for i in range(3)}
print(myMap)

# values only
for val in myMap.values()

# keys only
for key in myMap.keys()

# key, value pairs
for key, val in myMap.items()

```

## Tuples
```python
tup = (1,2,3)
print(tup)
print(tup[0]) # 1

tup[0] = 0 # can't modify

# utilize the immutable nature and use tuples as keys for hashmaps
myMap = {(1,2): '3'}

# add to sets:
mySet = set()
mySet.add((1,2))
print((1,2) in mySet)

# lists can't be keys -> mutable
```

## Heaps
```python
import heapq

# heaps are arrays under the hood
minHeap = []
heapq.heappush(minHeap, 3)
heapq.heappush(minHeap, 2)
heapq.heappush(minHeap, 4)

print(minHeap[0]) # 2 

while len(minHeap):
	print(heapq.heappop(minHeap))

# no max heaps by default, work around is to use -1 when push & pop
maxHeap = []
heapq.heappush(maxHeap, -3)
heapq.heappush(maxHeap, -2)
heapq.heappush(maxHeap, -4)

print(maxHeap[0] * -1)

while len(minHeap):
	print(-1 * heapq.heappop(maxHeap))

# build heaps from initial values
arr = [2, 1, 8, 4, 5]
heapq.heapify(arr)
```



