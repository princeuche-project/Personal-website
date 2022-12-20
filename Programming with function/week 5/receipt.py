import csv
from datetime import datetime
from calendar import weekday
PRODUCT_INDEX = 0
pro_unm = 7
def main():
    current_date_and_time = datetime.now()
    weekday = current_date_and_time.weekday()
    # Calls the read_dict function and stores the compound dictionary in a variable 
    # named products_dict.

    products_dict = read_dict('products.csv', PRODUCT_INDEX )

    # Prints the products_dict.
    print()
    print('All products')
    print()
    print(products_dict)
    print()
    # Print the store name at the top of the receipt.
    print('Inkom Emporium')
    print()
    print('Requested items')
   
    
    with open('request.csv', 'rt') as request_file:
        reader = csv.reader(request_file)
        next(reader)
        subtotal = 0.00
        sale_tax =.06
        number = 0
    #Uses a loop that reads and processes each row from the request.csv file. Within the body of the loop,
    #  your program must do the following for each row: 
        for line in reader:
          line_id = line [0]
          line_amount = int(line[1])
          line_product_name = products_dict[line_id][1]
          line_product_price = float(products_dict[line_id][2])
          number += line_amount
          subtotal += line_product_price * line_amount 
          print(f'{line_product_name}: {line_amount} @ {line_product_price}')
    sale_tax = subtotal * sale_tax
    total = subtotal + sale_tax
    print()
    # Sum and print the number of ordered items.
    print(f'Number of items: {number}')
    # Sum and print the subtotal due.
    print(f'Subtotal: ${subtotal:.2f}')
    # Compute and print the sales tax amount. Use 6% as the sales tax rate.
    print(f'Sale Tax: ${sale_tax:.2f}') 
    # Compute and print the total amount due.  
    print(f'Total: ${total:.2f}')
    print()
    # Print a thank you message.
    print('Thank you for shopping at the Inkom Emporium.')
    # Get the current date and time from your computer’s operating system and print the current date and time.
    print(f" {current_date_and_time:%A %b %I:%M %p %Y}")
    print()
    print('We are offering discount every Tuesdays and Wednesdays' )
    if weekday == 1 or weekday == 2: 
        discount = round(subtotal * 0.10)
        print(f'Discount amount: ${discount:.2f}')
        subtotal -= discount
        discount_pay = total - discount
        print(f'Total amount for discount pay: $ {discount_pay:.2f}')
    print()
    print('Your survey will help us to improve more and serve you better.')
    
    #Include a try block and except blocks to handle FileNotFoundError, PermissionError, and KeyError.
    try:
        filename   = products_dict
        read_dic =  (filename, PRODUCT_INDEX )
        #line_product_name = products_dict[line_id][pro_unm]           
    except KeyError as key_err:
         print(type(key_err).__name__, key_err, sep=": ")

         print(f'Error: unknown product ID in the request.csv file {read_dic}')
               
    except FileNotFoundError as file_not_fun_err:
        print(type(file_not_fun_err).__name__, file_not_fun_err, sep=": ")
        print(f'The file does not exit{read_dic}')

    except PermissionError as permission_err:
       # read_dic =  read_dict(filename, PRODUCT_INDEX )
        print(type(permission_err).__name__, permission_err, sep=": ")
        print(f'You are not permitted to open this file {read_dic}')

    answer = input('Were you satistify with our products and services? (YES/NO) ').lower().strip()

    if answer == 'yes':
        print()
        print("Thanks very much for the survey! We are always at your service to serve you well.")
    elif answer == 'no':
        print()
        print('We are very sorry for the inconvennience, We promise to  serve you better and to improve.')
    else:
        print()
        print('Invalid option')
          
def read_dict(filename, product_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    products_dict = {}

    with open(filename, 'rt') as products_file:
        reader = csv.reader(products_file)
        next(reader)
        for products in reader:
            products_dict[products[product_index]]  = products

    return products_dict

if __name__ == "__main__":
    main()
