# friends = []



# names = ""

# while names != "end":
#     names = input('What is your friend name? ')
#     if names != 'end':
#         friends.append(names)
    

# for i in friends:
#     if names == "end":
#         print('')
#     print(i.title())

print('Welcome to the shopping cart')

cart = []
prices = []
price = 0
total = 0


while True:
    print()
    print('1. Add a new item')
    print('2. Display the contents of the shopping cart')
    print('3. Remove an item')
    print('4. Compute the total')
    print('5. Quit')

    item = " "
    select = int(input('Please enter a number of choice: '))
    

    if select == 1:
        while item != 'quit':

          item = input('What item would you like to add? ')
          price = float(input('what is the price of the item? '))
          prices.append(price)
          cart.append(item)
          total += price
          print(f"'{item}' has been added to the cart." )
          print(f'The price is ${price:.2f}')
          break
   
   
    if select == 2:
# getting the list of all items in the shopping cart.

        print('This is what in your shopping cart.')
        for i in range(len(prices)):
            item = cart[i]
            price = prices[i]
            print(f"{i}. {item} - ${price}")
                
    if select == 3:
      
        takeout = input('Which item would you like to remove? ')
        item = cart
        cart.pop(int(takeout))
        prices.pop()
        print(f'What you have in your cart now is:  ')
        print(cart)
        continue
    
    if select == 4:
      print('Check the total price of your items')
      for price in prices:
        print(f'\nThe total price of your goods is:')
        print(f'\nTotal: ${total:.2f}')
        break

    if select == 5:
        print('you are about to quit. ')
        answer = input('Do you want to quit? (yes/no) ')

        if answer != 'yes':
            print('Please choose from the list. ')  
        else:
            print(f'Thanks very much for shopping with us!')
            break
       


