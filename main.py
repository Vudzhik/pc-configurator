from logic import add_item, remove_item
видеокарты = {'Nvidia' : ['RTX 5050', 'RTX 5060', 'RTX 5070', 'RTX 5070ti'],
              'Radeon AMD' : ['RX 9070 XT', 'RX 9060 XT', 'RX 7600 XT' ],
              'Intel' : ['Arc B580', ' Arc Pro B50', 'Arc A750']}
процессоры = {'Intel' : ['Core i5 12400f', 'Core i3 14100', 'Core Ultra 7'],
              'AMD' : ['Ryzen 9 9950X3D', 'Ryzen 7 9800X3D', 'Ryzen 5 7500F']}
def список_возможностей():
    running = True
    while running:
        print("\nВведите 'видеокарты', 'процессоры', 'добавить', 'удалить' или 'выход':")
        guess=input().lower()
        if guess == 'видеокарты':
            for brand, models in видеокарты.items():
                print(f'Бренд: {brand}')
                print(f'Модели: {models}')
        elif guess == 'процессоры':
            for brand, models in процессоры.items():
                print(f'Бренд: {brand}')
                print(f'Модели: {models}')
        elif guess == 'выход':
            print('\nВыход произведён успешно!')
            running = False
        elif guess == 'добавить':
            adding = True
            while adding:
                print('\nКуда будем добавлять? На выбор есть видеокарты и процессоры, либо назад.')
                guess = input().lower()
                if guess == 'видеокарты':
                    adding = add_item(видеокарты, 'видеокарт')
                elif guess == 'процессоры':
                    adding = add_item(процессоры, 'процессоров')
                elif guess == 'назад':
                    adding = False
                else:
                    print('Пожалуйста, введите правильное значение.')
        elif guess == 'удалить':
            deleting = True
            while deleting:
                print('\nЧто будем удалять? На выбор есть видеокарты и процессоры, а так же назад')
                guess = input().lower()
                if guess == 'видеокарты':
                    deleting = remove_item(видеокарты, 'видеокарт')
                elif guess == 'процессоры':
                    deleting = remove_item(процессоры, 'процессоров')
        else:
            print('\nПожалуйста, введите один из существующих параметров.')
список_возможностей()