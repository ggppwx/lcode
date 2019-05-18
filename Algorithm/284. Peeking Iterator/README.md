# Problem
[Peeking Iterator](https://leetcode.com/problems/peeking-iterator)

Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().

Example:
```
Assume that the iterator is initialized to the beginning of the list: [1,2,3].
Call next() gets you 1, the first element in the list.
Now you call peek() and it returns 2, the next element. Calling next() after that still return 2. 
You call next() the final time and it returns 3, the last element. 
Calling hasNext() after that should return false.
```
Follow up: How would you extend your design to be generic and work with all types, not just integer?

## Analysis
Time: O(n)

## Thoughts
- Designing the interface is the hard part 
- Watch out typo 
- If you wanna make desgin generic, using template. 
  - No need to worry in python 

## Solution
```python
# Below is the interface for Iterator, which is already defined for you.
#
# class Iterator:
#     def __init__(self, nums):
#         """
#         Initializes an iterator object to the beginning of a list.
#         :type nums: List[int]
#         """
#
#     def hasNext(self):
#         """
#         Returns true if the iteration has more elements.
#         :rtype: bool
#         """
#
#     def next(self):
#         """
#         Returns the next element in the iteration.
#         :rtype: int
#         """
class PeekingIterator:
    def __init__(self, iterator):
        self._nums = []
        # getting all items of iterator
        while iterator.hasNext():
            self._nums.append(iterator.next())
        self._currentPos = -1

    def peek(self):
        return self._nums[self._currentPos + 1]

    def hasNext(self):
        return self._currentPos + 1 < len(self._nums)        
    
    def next(self):
        self._currentPos += 1
        return self._nums[self._currentPos]
        

```
## Tags
Design

## Marks

[comment]: <timestamp:2019-05-18>