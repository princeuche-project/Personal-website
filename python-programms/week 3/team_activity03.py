from math import pi
from turtle import width

# #variables for square

# side_square = float(
#     input('What is the length in cm of the side of a square? '))
# print(
#     f'The area of the square is {side_square ** 2} sq cm or {side_square ** 2 / 10000} sq m.')

# rect_length = float(input('What is the length in cm of the rectangle? '))
# rect_width = float(input('What is the width in cm of the rectangle? '))
# print(
#     f'The area of the rectangle is {rect_length * rect_width} sq cm or {rect_length * rect_width / 10000} sq m.')

# radius = float(input('What is the radius in cm of a circle? '))
# print(
#     f'The area of the circle is {radius ** 2 * pi} sq cm or {radius ** 2 * pi / 10000} sq m.')

# measure = float(input('What is the measurement? '))

# # square
# print(f'The area of the square is {measure ** 2}.')

# # circle
# print(f'The area of the circle is {measure ** 2 * pi}.')

# # volume cube
# print(f'The volume of the square is {measure ** 3}.')

# # volume sphere
# print(f'The volume of the sphere is {4/3 * pi * (measure ** 3)}.')


# side = float(input('what is the lenght of a side of the squre in cm '))
# area = side **2
# side = 'the are of the squre is {} '
# print(f'the are of the squere is {area}')
# print(side.format(area))

# lenght = float(input('what is the of rectangle in cm? '))
# width = float(input('what is the of rectangle in cm? '))
# area = lenght * width
# lp = ' the areas of the rectangle is {}'
# print(lp.format(area))

# radius = float(input(' what is the radius of the circle ?'))
# area = 3.14 * (radius ** 2)
# lp = 'the area of the circle is: {}'
# print(lp.format(area))

import math
('--------------------------------------------')
print()

print('Welcome tothe velocity calculation. Please enter the fellowinf:/n ')
m = float(input('Mass (in kg) '))
print()
g = float(input('Gravity (in m/s^2, 9.8 for earth, 24 for jupiter): '))
print()
t = float(input('Time (in seconds): '))
print()
p = float(input('Density of the fluid (in kg/m^3 for air, 1000 for water): '))
print()
a = float(input('Cross sectional area (in m^20; '))
print()
c = float(input('Drag consant (0.5 for sphere, 1.1 for cylinder): '))

print()

c = (1/2)* p * a * c
v = math.sqrt(m * g / c) * (1 - math.exp((-math.sqrt(m * g * c)/ m) * t))
print()
print(f'The inner value of c is: {c:.3f}')
print(f'The velosity  after {t} seconds is: {v:.3f} m/s')