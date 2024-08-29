import copy
fruits = ['apples', 'oranges', 'strawberries', 'kiwi', 'grapes']
print(fruits)

my_fruits_copy = copy.deepcopy(fruits)

my_fruits_copy.append('bananas')
print('\nAdding Bananas to ou deep copied list')
print(f'Fruits = {fruits}')
print(f'My fruits = {my_fruits_copy}\n')
print(fruits)
