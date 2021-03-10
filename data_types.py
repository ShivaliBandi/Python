x = "Hello World"#	str	
print(type(x))
x = 20#	int	
print(type(x))

x = 20.5#	float	
print(type(x))

x = 1j#	complex	
print(type(x))

x = ["apple", "banana", "cherry"]#	list	
print(type(x))

x = ("apple", "banana", "cherry")#	tuple	
print(type(x))

x = range(6)#	range	
print(type(x))

x = {"name" : "John", "age" : 36}#	dict	
print(type(x))

x = {"apple", "banana", "cherry"}#	set	
print(type(x))

x = frozenset({"apple", "banana", "cherry"})#	frozenset	
print(type(x))

x = True#	bool	
print(type(x))

x = b"Hello"#	bytes	
print(type(x))

x = bytearray(5)#	bytearray	
print(type(x))

x = memoryview(bytes(5))#	memoryview	
print(type(x))
'''
If you want to specify the data type, you can use the following constructor functions:


x = str("Hello World")	str	
x = int(20)	int	
x = float(20.5)	float	
x = complex(1j)	complex	
x = list(("apple", "banana", "cherry"))	list	
x = tuple(("apple", "banana", "cherry"))	tuple	
x = range(6)	range	
x = dict(name="John", age=36)	dict	
x = set(("apple", "banana", "cherry"))	set	
x = frozenset(("apple", "banana", "cherry"))	frozenset	
x = bool(5)	bool	
x = bytes(5)	bytes	
x = bytearray(5)	bytearray	
x = memoryview(bytes(5))	memoryview	


'''