
print()
def main():
    liberaries = contact_save(numbers)
    ID_card = id_card_generator(2)
    print(ID_card)
    print(f"{liberaries}")
    print()

def id_card_generator(id):
      print('Please fill in your details.')
      print()
      company_n = 'empower energy solution'
      id_number = int(input('Enter your ID number: '))

      f_name =  input('What is your first name? ')
      m_name = input('what is your middle name? ')
      l_name = input('what is your last name? ')
      d_of_birth = input('What is your date of birth? ')
      gender = input('What is your gender? ')
      occupation = input('What is your job tille? ')
      country = input('Where are you from? ')
      joined_date = input('When is your joining date? ')
      expiring_date = input('Expiring date: ')
      email_address = input('Enter your email address: ')
      calling = '971-563-839-728'
      print()
      print(f'{company_n.upper()}')
      print()
      print(f'--------------- Employee ID No. {id_number} : -----------------')
      print(f'Name: {l_name.title()} {f_name.title()} {m_name.title()}')
      print()
      print(f'Date of Birth: {d_of_birth}')
      print()
      print(f'Gender: {gender.title()}')
      print()
      print(f'Country: {country.title():13} Ocupation: {occupation.title()}')
      print()
      print(f'Joining Date: {joined_date:13} Expiring Date: {expiring_date}')
      print()
      print(f'Email Address: {email_address}')
      print()
      print('If found, Please call')
      print(f'Tele: {calling}')
      print('Send it to P.O. Box 56341, Dubai 440077')
      print('-----------------------------------------------------------------')
      return id


# To store and save multiple multiple contacts

while True:
     print('PLease enter number 5 to see the cart menu: ')
     option = int(input("Please, enter an action: "))

     if option == 5:
         break   
def menu():
      print("1. Add a new item")
      print("2. Display the content of the shopping cart")
      print("3. Remove an item of the shopping cart")
      print("4. Compute total of the items in the shopping cart")
      print("5. Quit")

def add_item():
    name = input("What item would you like to add? ")
    price = float(input(f"What is the price of the {name}? "))
    cart.append( [name, price] )
    print(f"{name} has been added to the cart.")

def display_content():
    print("The content of the shopping cart are:")

    for name, price in cart:
        print(f"{name} - {price}")

def remove_item():
    selected_name = input("Which item would you like to remove? ")
    temp = []
    for name, price in cart:
        if name != selected_name:
            temp.append( [name, price] )
    cart = temp
    
def total_sum():
    summation = 0

    for name, price in cart:
        summation += price
        
    print(f'The total price of the items in the shopping cart is ${summation}')
# menu cart
cart = [] 

print("Welcome to the Shopping Cart Program!")
print()

while True:

    menu()
    option = int(input("Please, enter an action: "))

    if option == 5:
        break
    
    elif option == 1:
        add_item()
        
    elif option == 2:
        display_content()
        
    elif option == 3:
        remove_item()
        
    elif option == 4:
        total_sum()
        
    else:
        print("Invalid option, please, try again.")
        
print("Thank you for using the shopping cart program. Good bye!")

print()
names = []
contact_numbers = []
numbers = int(input("Enter the total number of contacts you want to save: "))

def contact_save(numbers):

  for i in range(numbers):
    name = input("Name: ")
    contact_number = int(input("Contact Number: ")) 
    names.append(name)
    contact_numbers.append(contact_number)
  print("\nName\t\t\tContact Number\n")
  for i in range(numbers):
       print("{}\t\t\t{}".format(names[i], contact_numbers[i]))
  return numbers
print()
if __name__ == "__main__":
    main()

