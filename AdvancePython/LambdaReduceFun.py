# Use reduce function and an appropriate lambda to find the maximum number in a list.
lst=[1,2,3,4,55,20]
import functools
print(functools.reduce(lambda x,y: x if x>y else y,lst))


