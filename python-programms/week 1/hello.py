color = input("please enter your favourite color:")
print("your favourite color is:")
print(color)

food = input("please enter your best meal:")
print("your best meal is:")
print(food)

country_capital = input("please enter the capital city of your country:")
print("The capital city of your county is:")
print(country_capital)

daily_activities = input("please tell us your daily activities:")
print("your daily activities are:")
print(daily_activities)
print("Thanks see you next time!")

first_name = input('what is your first name?')
last_name = input('what is your last name?')
print(f' your name is{last_name}, {first_name} {last_name}.')


print(' Please enter the following information:')
print()
# A programme that generate an ID card
first_name = input('First name:')
last_name = input('last name:')
email_address = input('email address:')
phone_number = input('phone number:')
job_tittle = input('job tittle:')
id_number = input('enter your ID number:')
hair = input('enter your hair color:')
month = input('date of joining:')
eye = input('eye color')
training = input('have you under go any training? Yes or No:')
print('The ID Card is:')
print('----------------------------------------------')
print(f'{last_name.upper()}, {first_name.title()} ')
print(f'{job_tittle.title()}')
print(f'ID:{id_number}')
print()
print(f'Email:{email_address.lower()}')
print(f'Contact:{phone_number}')

print(f'Hair color:{hair.title():15} Eyes collor:{eye.title()}')
print(
    f'month joined:{month.title():14} Additional training completed:{training.title()}')

print('-------------------------------------------------------------')

noun = input('enter')
animal = input('enter an animal')
print('yopur story is:')
print()
print(
    f'the other day, i was really in the house {noun}, and every body were like {animal} it wea really bad.')
