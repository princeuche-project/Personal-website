# # from turtle import distance


# # x = "good"


# # def myfunc():
# #     print('python is ' + x)


# # myfunc()

# # x = 1j
# # print(x)

# # print(type(x))

# # x = dict(name="John", age=36)

# # # display x:
# # print(x)

# # # display the data type of x:
# # print(type(x))

# # x = 2
# # y = 3
# # z = 4
# # w = x + y * z
# # print(w)
# # #USING FORMAT STRINGS
# # car = 4
# # people = 5

# # peoplePerCar = people/car
# # print('there are {} people in a car'.format(peoplePerCar, ':.3f'))
# # print(f'the are {peoplePerCar:.3f} people in the car')

# # #Thousands Grouping
# # bigNumber = 2345678976
# # print(f'the big number is $ {bigNumber:,}')

# # #Scientific Notation
# # distance = 6*456*65
# # print(f'the distance is {distance:.3e}')

# # #USING THE MATH LIBRARY
# # import math

# # radius = 5
# # area =  math.pi * (radius ** 2)
# # c = 'the area is: {}'
# # print(c.format( area))
# # print(f"The area is: {area}")

#To convert degrees in Fahrenheit to Celsius
fahrenheit = int(input(' what is the tempreture in the Fahrenheit'))
celsius = (fahrenheit - 32) * 5 / 9
print(f'The temperature in Celsius is {celsius} degrees.')
print('The temperature in Celsius is {} degrees.' .format(celsius))

# # n = 0
# # while n < 5:
# #     print(n)
# #     n = n +2
     
# bread = float(input("How many qut of bread? "))
# price = float(input("How much for one? "))
# vat = 0.5
# bread_price = bread * price
# total = bread_price + vat
# print(f'Total: $ {bread_price + vat:,}' )

x = 5
x += 1
print(x)

x = ['aple', 'oranges', 'mangos']
print(x[2])
print(x)