"""
a sequence of non-negative integers could be transformed into a segment
 if the difference between adjacent elements of this sequence is equal to one. 
For example, the numbers 3,4,5,6,7,8 can be converted into a segment
[3;8]. The numbers 1,3,5,11,15,22 cannot be converted into a segment. 
A single number is transformed into a segment in which both the right 
and left boundaries are itself.
 For example, number 1 can be converted to the segment [1;1].

a ranges() function takes one argument:

numbers — a list of different natural numbers, arranged in ascending order
The function converts numbers from the numbers list into segments, 
representing them as tuples,
 where the first element of the tuple is the left border of the segment,
 the second element is the right border of the segment. 
The function must return the resulting segment tuples as a list.

The numbers in the list are returned by the function in their original order.
"""



from itertools import groupby
def ranges(numbers):
    a=groupby(sorted(numbers,key=lambda x: numbers.index(x) - x),
    key=lambda x: numbers.index(x)-x)
    result=[]
    for k,v in a:
        v=list(v)
        if len(v)==1:
            result.append((v[0],v[0]))
        else:
            result.append((v[0],v[len(v)-1]))
    return sorted(result,key=lambda x: x[0])

"""
Test samples
"""
numbers = [1, 3, 5, 7]

print(ranges(numbers))


mbers = list(range(5, 101))

print(ranges(numbers))


numbers = list(range(10, 21)) + [30] + list(range(35, 101)) + list(range(1000, 1001))

print(ranges(numbers))


numbers = [1, 2, 3, 4, 7, 8, 10]

print(ranges(numbers))
