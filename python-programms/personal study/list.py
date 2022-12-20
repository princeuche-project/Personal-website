# To access list items you have to reffer to the list number
# list = ['rice', 'bean', 'oranges', 'oil', 'phone']
# print(list[0])
# print(len(list))

# # To check if items is in the list
# if 'bean' in list:
#     print('yes beans is in the list')
# # To change the list items
# list[2] = 'banana'
# print(list)
# # To change the range of item value
# list[2:4] = ['laptop', 'computers']
# print(list)

#To remove a list from the item value. (use the pop, remove, and del method)
list = ['rice', 'bean', 'oranges', 'oil', 'phone']
list.remove('oil')
print(list)

#Using a While Loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
#List Comprehension
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "e" in x:
    newlist.append(x)

print(newlist)
#To sort an items in alphanumerical ascendent value
x = ['u', 'c', 'h', 'e' 'n' 'n' 'a']
x.sort()
print(x)
#To sort an items in alphanumerical decendent value
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

# To join two list together
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)


