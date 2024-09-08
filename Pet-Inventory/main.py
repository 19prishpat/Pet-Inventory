in_stock = ['cat']

while True:
    print('Menu')
    print('1. Pet addition')
    print('2. Pet removal')
    print('3. Inventory check')
    print('4. exit')

    decision = input('Enter the number of the option you choose:')

    if decision == '1':
        pet = input('New pet to inventory: ')
        in_stock.append(pet)
    elif decision == '2' :
        pet = input('What pet is to be removed: ')
        if pet in in_stock:
            in_stock.remove(pet)

        else:
            print('The pet is not in stock')

    elif decision == '3':
        for pet in in_stock:
            print(pet)

    elif decision == '4':
        break