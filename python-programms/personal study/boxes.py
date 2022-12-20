# How to use the buit-in function called math.ceil
import math

num_item = int(input('Enter the number of iteams: '))
box = int(input('Enter the number of iteams per box: '))
num_item_box = math.ceil(num_item / box)

print(f'for {num_item} items, packing {box} items in each box you will need {num_item_box} boxes. ')