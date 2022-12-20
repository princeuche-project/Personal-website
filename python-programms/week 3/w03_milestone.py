

age = int(input('How old are you?'))
next_year = age + 1
print(f'on your next birthday, you will be {next_year}')
print()

carton = int(input('how many eggs are in the carton?'))
eggs = carton * 12
print(f'you have {eggs} eggs')

print()
cookies = int(input('\nhow many cookies do you have?'))
people = int(input('how many people are there?'))
cookies_per_person = cookies/people
c = 'each person will have {} cokkies'
print(c.format(cookies_per_person))
print(f'each person many have {cookies_per_person} cookies')
print()

# Meal price calculator

child_meal = float(input('what is the price of the child meal? '))
print()
adult_meal = float(input('what is the price of the adult meal? '))
print()
num_children = int(input('how many children are there? '))
print()
num_adult = int(input('how many adult are there? '))
print()
sale_tax = float(input('what is the sale tax rete? '))
print()
subtotal = child_meal * num_children + adult_meal * num_adult
print(f'Subtotal: $ {subtotal:,.2f}')
sale = subtotal * sale_tax / 100
print(f'Sale tax: $ {sale:,.2f}')
total = subtotal + sale
print(f'Total: $ {total:,.2f}')
print()
amount_paid = float(input('please enter paid amount:' ))
print(f'Change: $ {total - amount_paid:,.2f}')
