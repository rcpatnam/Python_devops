name = ''
price = ''
items = {}
while name != 'bye':
    name = input('enter name: ')
    if name == 'bye':
        break
    else:
        price = float(input('enter name: '))
        items[name] = price
print(items)









