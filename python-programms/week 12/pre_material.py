# shopping_cart = [
#     ["Chips", 2.99],
#     ["Bread", 2.50],
#     ["Milk", 3.19],
#     ["Ice Cream", 6.99],
#     ["Cheese", 5.99],
#     ["Candy bar", 0.99]
# ]

# max_price = -1

# for item in shopping_cart:
#     price = item[1] # The price is the second part of the item

#     if price > max_price:
#         # This is the new max
#         max_price = price

# print(f"The maximum price is: {max_price}")

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

youngest = 10
youngest_name = ''
for i in people:
    parts = i.split(' ')
    name = parts[0]
    age = float(parts[1])
    print(name)
    if age < youngest:
        youngest = age
        youngest_name = name
        
print(youngest, youngest_name)



 formula = input("Enter a formula for a molecule: ")
            formula_dict = parse_formula(formula)
            print(f"{round(molar_mass(formula_dict),5)} grams/mole")
            get_mass = float(input("Enter a mass in grams: "))
            moles = round(get_mass/molar_mass(formula_dict),5)
            print(f"{moles} moles")