#Getting the Data Type
x = 5
y = 'hello word'
z = 2.9
a = ['uche', ' emeka', 'chima']
w = ('uche', 'uche', 'chima')

print(type(y))
print(type(x))
print(type(z))
print(type(a))
print(type(w))

#Convert from one type to another:

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = complex(x)

print(a)
print(b)
print(c)

print(type(a))
print(type(b))
print(type(c))
print()

x = complex(input(' anything type'))
print(x)
print(type(x))