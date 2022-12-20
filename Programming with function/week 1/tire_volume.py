import math
from datetime import datetime, tzinfo
from re import M
current_date = datetime.now()

w = float(input('Enter the width of the tire in mm (ex 205): '))
a = float(input('Enter the aspect ratio of the tire (ex 60): '))
d = float(input('Enter the diameter of the wheel in inches (ex 15): '))
print()
v = (math.pi * (w**2 * a *(w * a + 2540 * d)))/10000000000
tire_price = 3343.20
tire_price2 = 2000
print(f'The approximate volume is {v:.2f} liters')
print()

if v >= 30:
  print(f'The price is: {tire_price:.2f}')
elif v <= 20:
  print(f'The price is: {tire_price2}')
else:
  print(v)

answer = input('Would you want to buy the tire? (Yes/No)')

with open('volume.txt', 'at') as volume_file:
  print(f'{current_date:%y-%m-%d}, {w}, {a}, {d}, {v:.2f}', file=volume_file)
  print()
  print('width of the tire:', w, file=volume_file)
  print()
  print('aspect ratio of the tire:', a, file=volume_file)
  print()
  print('diameter of the wheel:', d, file=volume_file)
  print()
  print(f'volume of the tire: {v:.2f}', file=volume_file)

  if answer == 'yes':
    phone_number = int(input('please enter you phone number '))
    print('The customer phone number is:', phone_number, file=volume_file)
  
 





















# f = 15
# g = 7.6
# h = f + g
# print(type(h))

# k = input("Please enter a integer: ")
# m = input("Please enter another integer: ")
# n = k + m
# print(type(n))

# a = 1
# b = 3
# c = -2
# result = a + b * 7 % 4 - c
# print(f'{result}')

# c = 15
# s = f"You found {c} coins."
# print(type(s))

# import random



# wordChosen = 'uchenna'


# display = wordChosen
# for i in range (len(display)):
#   display = display[0:i] + "_" + display[i+1:]
  
# print ( 'you hint is :' , display )


# attempts = 1

# while display != wordChosen:
#   guess = input("Please enter a letter: ")
#   guess = guess
  
  
#   for i in range(len(wordChosen)):
#     if wordChosen[i] == guess:
#       display = display[0:i] + guess + display[i+1:]

#       print(" ", (display.upper()))
#       attempts = attempts + 1
  
# print("Well done, you guessed right!")
# print(f"it took you {attempts}")
