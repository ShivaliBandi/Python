'''
List
Lists are used to store multiple items in a single variable.

Lists are one of 4 built-in data types in Python used to store collections of data, 
the other 3 are Tuple, Set, and Dictionary, all with different qualities and usage.

Lists are created using square brackets:
List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc.

'''
thislist = ["apple", "banana", "cherry"]
print(thislist)

#To determine how many items a list has, use the len() function:
print(len(thislist))

#From Python's perspective, lists are defined as objects with the data type 'list':

print(type(thislist))
