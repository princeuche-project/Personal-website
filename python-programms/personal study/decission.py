

product = input('please enter the purchased item ')
price = float(input('please enter the price of the product '))
tax = 0.5
pricetax = price + tax
if product in ("Clothe, phone, bag, shirt,"):
    price < 30
    tax = 0.1
elif product in ('Lapto, computer, radio'):
    price > 50
    tax = 0.5
else: 
    price >= 10
    tax = 0.0
print(pricetax)
print(tax)
 

province = input('what province do you live in? ')
tax = 0
if province == 'Imo':
    tax = 0.8
elif province == 'Lagos':
    tax = 0.75
elif province == 'Aba':
    tax = 0.90
else:
    tax = 0.0
print(tax)

x = 6
y = 6
if x == 5:
    print('a')
    if y == 6:
        print('b')
else:
    print('c')
    if y == 10:
     print('d')

print('Please ent the following to be qualify for the loan. ')
print()

loan_size = float(input('How large is the loan? '))
credit_hostory = float(input('How good is your credit history? '))
income = float(input('How high is your income? '))
down_payment = float(input('How large is your down payment? '))
print()
should_loan = False

if loan_size >= 5:
    if credit_hostory >= 7 and income >= 8:
        should_loan = True
    elif credit_hostory >= 7 or income >= 7:
        if down_payment >= 5:
                should_loan = True
                print('yes you are qualified')
        else:
             should_loan = False 
else:
    if credit_hostory < 4:
        should_loan = False
    else:
        if income >= 7 or down_payment >= 7:
            should_loan = True
        elif income >= 4 and down_payment >= 4:
            should_loan = True
        else: 
            should_loan = False 
if should_loan:
    print('you are qualified' )       
else:
    print(' you are not qualified')






