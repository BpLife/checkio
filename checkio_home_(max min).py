# 
# In this mission you should write you own py3 implementation of the built-in functions min and max. Some builtin functions are closed here: import, eval, exec, globals. Don't forget you should implement two functions in your code.
# 
# max(iterable, *[, key]) or min(iterable, *[, key])
# max(arg1, arg2, *args[, key]) or min(arg1, arg2, *args[, key])
# 
# Return the largest (smallest) item in an iterable or the largest(smallest) of two or more arguments.
# 
# If one positional argument is provided, it should be an iterable. The largest (smallest) item in the iterable is returned. If two or more positional arguments are provided, the largest (smallest) of the positional arguments is returned.
# 
# The optional keyword-only key argument specifies a function of one argument that is used to extract a comparison key from each list element (for example, key=str.lower).
# 
# If multiple items are maximal (minimal), the function returns the first one encountered.
# 
# -- Python Documentation (Built-in Functions)
# 
# Input: One positional argument as an iterable or two or more positional arguments. Optional keyword argument as a function.
# 
# Output: The largest item for the "max" function and the smallest for the "min" function.
# 
# Example:
# 
# ?
# 1
# 2
# 3
# 4
# 5
# 6
# max(3, 2) == 3
# min(3, 2) == 2
# max([1, 2, 0, 3, 4]) == 4
# min("hello") == "e"
# max(2.2, 5.6, 5.9, key=int) == 5.6
# min([[1,2], [3, 4], [9, 0]], key=lambda x: x[1]) == [9, 0]
# How it is used: This task will help you understand how some of the built-in functions work on a more precise level.

#the one
import types
def max(*args, **kwargs):
    key = kwargs.get("key", None)
    if isinstance(args[0],types.GeneratorType):
        b = args[0]
        largest = next(b)
        for x in b:
            if largest < x:
                largest = x
        return  largest
    elif hasattr(args[0], '__iter__'):
        b = list(args[0])
        largest = b[0]
        for x in b:
            if key == None:
                if largest < x:
                    largest = x
            else:
                if key(largest) < key(x):
                    largest = x
        return largest
    else:
        largest = args[0]
        for x in args:
            if key == None:
                if largest < x:
                    largest = x
            else:
                if key(largest) < key(x):
                    largest = x
        return largest

def min(*args, key=None, **kwargs):
    key = key
    if isinstance(args[0],types.GeneratorType):
        b = args[0]
        smallest = next(b)
        for x in b:
            if smallest > x:
                smallest = x
        return  smallest
    elif hasattr(args[0], '__iter__'):
        b = list(args[0])
        smallest = b[0]
        for x in b:
            if key == None:
                if smallest > x:
                    smallest = x
            else:
                if key(smallest) > key(x):
                    smallest = x
        return smallest
    else:
        smallest = args[0]
        for x in args:
            if key == None:
                if smallest > x:
                    smallest = x
            else:
                if key(smallest) > key(x):
                    smallest = x
        return smallest

print(max([1, 2, 3], [5, 6], [7], [0, 0, 0, 1]))



#two
def minSimple(arg1, arg2, key):
    if key != None and key(arg1) <= key(arg2) or key == None and arg1 < arg2:
        return arg1
    return arg2
def maxSimple(arg1,arg2,key):
    if key != None and key(arg1) >= key(arg2) or key == None and arg1 > arg2:
        return arg1
    return arg2

def max(*args, key=None):
    l = len(args)
    if l == 1:
        args = list(args[0])
        l = len(args)
    result = args[0]
    for i in range(1,l):
        result = maxSimple(result,args[i],key)
    return result
def min(*args, key=None):
    l = len(args)
    if l == 1:
        args = list(args[0])
        l = len(args)
    result = args[0]
    for i in range(1,l):
        result = minSimple(result, args[i], key)
    return result


#three
def get_first_from_sorted(args, key, reverse):
    if len(args) == 1:
        args = iter(args[0])
    return sorted(args, key=key, reverse=reverse)[0]


def min(*args, key=None):
    return get_first_from_sorted(args, key, False)


def max(*args, key=None):
    return get_first_from_sorted(args, key, True)
print(max(2.2, 5.6, 5.9, key=int))
