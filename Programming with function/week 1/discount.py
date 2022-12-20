from calendar import weekday
from datetime import datetime, timedelta 

current_time = datetime.now()
weekday = current_time.weekday()

subtotal = float(input('Please enter the subtotal: '))


 

if subtotal >= 50 and (weekday == 1 or weekday == 2): 
    discount = round(subtotal * 0.10)
    print(f'Discount amount: ${discount:.2f}')
    subtotal -= discount
if subtotal <= 20:
  saleTax = round(subtotal * 0.06)
  saleTax = 0
  print(f'Sales tax amount: ${saleTax:.2f}')
else:
    
    saleTax = round(subtotal * 0.06)
    print(f'Sales tax amount: ${saleTax:.2f}')
total =  round(subtotal + saleTax)
print(f'Total: ${total:.2f}')



word = 'uchenna'
number_letter = 7
for index in range(number_letter):
  letter = word [index]
  print(index, letter)

colors = ["red", "blue", "green", "yellow"]
for color in colors:
  print(color)
for number in range(1,9):
  print(number)

for i in range(2,21, 2):
  print(i)



