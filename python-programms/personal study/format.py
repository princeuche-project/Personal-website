#Use the format() method to insert numbers into strings:

name = 'uche'
age = 26
nameAge = '{0} {1}'
print(nameAge.format(name.capitalize(), age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

quantity = 3
itemno = 567
price = 49.95
print(f'i want to pay {quantity} pieces of items {itemno} for {price} dollars.')

quantity = 3
itemno = 567
price = 49.95
itemno = quantity * price
print(f'Total: {itemno}')
