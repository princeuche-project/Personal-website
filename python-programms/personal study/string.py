# how to get the lenght of a string.
from calendar import c


x = 'hello my friend, how are you?'
print(x)
print(len(x))

# How to check if a string is in a text by using the word (in)
text = 'today is going to be a better day for all of us'
print('better' in text)

# how to use an (if) statement to check if string is in a text.

text = 'today is going to be a better day for all of us'
if 'better' in text:
    print('yes, "better" is present')

# how to use the + operator to concatenate strings

a = 'hello'
b = 'how are you'
print(f'{a +" " + b}')

a = 'hello'
b = 'how are you'
c = a + " " + b
print(c)

# strings are immutable. you can change the letter of a strings.

x = 'uchenna'
c = 'G' + x[1:len(x)]
print(c)
print(x.replace('u', 'G'))

a = 'hello world'
print(a[-1])
# to slice a string either from start or end
print(a[4:5])

x = 10
y = 4
if x < y:
  print('y is less that x')
else:
  print('x is greater')

  print(bool('hello world'))

import math

def areaof_radius(radius, height):
  volume = math.pi * radius **2 * height
  print (f'the volume is: {volume}')
areaof_radius(2.4, 4.1)


# Example 2

# import math

# # Define a function named print_cylinder_volume.
# def print_cylinder_volume(radius, height):
#     """Compute and print the volume of a cylinder.
#     Parameters
#         radius: the radius of the cylinder
#         height: the height of the cylinder
#     Return: nothing
#     """
#     # Compute the volume of the cylinder.
#     volume = math.pi * radius**2 * height

#     # Print the volume of the cylinder.
#     print(volume)
# print_cylinder_volume(2.4, 4.1)