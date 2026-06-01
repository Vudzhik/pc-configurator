import logic

def main_menu():
    running = True
    while running:
        print('\n' + '='*45)
        print('             УПРАВЛЕНИЕ БАЗОЙ ПК')
        print('='*45)
        print(' [1] 📋 Посмотреть список товаров')
        print(' [2] 🔍 Поиск компонента')
        print(' [3] ⚙️ Текущая сборка ПК (корзина)')
        print(' [4] 📥 Сохранить базу и сборку')
        print(' [5] ➕ Добавить новую деталь в магазин')
        print(' [6] ➖ Удалить деталь из магазина')
        print("-" * 45)
        print(" [0] 👋 Выход из программы")
        print("=" * 45)
        main_choice = input('Выберите номер действия\n').strip()

        if main_choice == '1':
            viewing = True
            while viewing:
                print('--- ВЫБЕРИТЕ КАТЕГОРИЮ ЖЕЛЕЗА ---')
                print(' [1] 🎮 Видеокарты (GPU)')
                print(' [2] 🧠 Процессоры (CPU)')
                print(' [3] 🧱 Материнские платы')
                print(' [4] 📟 Оперативная память (RAM)')
                print(' [5] 💾 Твердотельные накопители (SSD)')
                print('-'*45)
                print(' [6] 🌐 Показать вообще всё')
                print(' [0] ⬅️ Назад')
                sub_choice = input('Выберите номер действия\n').strip()
                if sub_choice == '1':
                    logic.details_list('видеокарты', 'видеокарт')
                    logic.add_question()
                elif sub_choice == '2':
                    logic.details_list('процессоры', 'процессоров')
                    logic.add_question()
                elif sub_choice == '3':
                    logic.details_list('материнские_платы', 'материнских плат')
                    logic.add_question()
                elif sub_choice == '4':
                    logic.details_list('оперативная_память', 'оперативной памяти')
                    logic.add_question()
                elif sub_choice == '5':
                    logic.details_list('ссд', 'ссд')
                    logic.add_question()

                elif sub_choice == '6':
                    logic.details_list('видеокарты', 'видеокарт')
                    logic.details_list('процессоры', 'процессоров')
                    logic.details_list('материнские_платы', 'материнских плат')
                    logic.details_list('оперативная_память', 'оперативной памяти')
                    logic.details_list('ссд', 'ссд')
                    total_price = 0
                    for category in logic.database:
                        for brand in logic.database[category]:
                            for item in logic.database[category][brand]:
                                total_price += item.price
                    print(f"\n===============================")
                    print(f"ОБЩАЯ СТОИМОСТЬ ЖЕЛЕЗА В БАЗЕ: {total_price}$")
                    print(f"===============================")
                    logic.add_question()

                elif sub_choice == '0':
                    viewing = False

                else:
                    print('Пожалуйста, введите верное значение!')

        elif main_choice == '2':
            logic.global_search()

        elif main_choice == '3':
            logic.user_build()

        elif main_choice == '4':
            logic.save_data()
            logic.save_build()
            print('Данные успешно сохранены!')

        elif main_choice == '5':
            while True:
                print('\n--- ➕ ДОБАВЛЕНИЕ ДЕТАЛИ: ВЫБЕРИТЕ КАТЕГОРИЮ ---')
                print(' [1] 🎮 Видеокарты (GPU)')
                print(' [2] 🧠 Процессоры (CPU)')
                print(' [3] 🧱 Материнские платы')
                print(' [4] 📟 Оперативная память (RAM)')
                print(' [5] 💾 Твердотельные накопители (SSD)')
                print('-' * 45)
                print(' [0] ⬅️ Назад')
                choice = input('Выберите номер действия\n').strip()
                if choice == '0':
                    print(' ❌ Добавление отменено')
                    break
                elif choice == '1':
                    category = 'видеокарты'
                elif choice == '2':
                    category = 'процессоры'
                elif choice == '3':
                    category = 'материнские_платы'
                elif choice == '4':
                    category = 'оперативная_память'
                elif choice == '5':
                    category = 'ссд'
                else:
                    print(' 🚫 Ошибка: Такого номера категории не существует. Попробуй ещё раз.\n')
                    continue
                brand = input('Введите бренд: \n').lower()
                name = input('Введите модель: \n').lower()
                while True:
                    try:
                        price = float(input('Введите цену: \n'))
                        break
                    except ValueError:
                        print(' 🚫 Ошибка! Вводите только цифры (например, 150 или 150.5')
                logic.adding(category, brand, name, price)
                break

        elif main_choice == '6':
            deleting = True
            while deleting:
                print('\n--- ➖ УДАЛЕНИЕ ДЕТАЛИ: ВЫБЕРИТЕ КАТЕГОРИЮ ---')
                print(' [1] 🎮 Видеокарты (GPU)')
                print(' [2] 🧠 Процессоры (CPU)')
                print(' [3] 🧱 Материнские платы')
                print(' [4] 📟 Оперативная память (RAM)')
                print(' [5] 💾 Твердотельные накопители (SSD)')
                print('-' * 45)
                print(' [0] ⬅️ Назад')
                sub_choice = input('Выберите номер действия\n').strip()

                if sub_choice == '1':
                    logic.deleting_part('видеокарты', 'видеокарты')
                elif sub_choice == '2':
                    logic.deleting_part('процессоры', 'процессора')
                elif sub_choice == '3':
                    logic.deleting_part('материнские_платы', 'материнской платы')
                elif sub_choice == '4':
                    logic.deleting_part('оперативная_память', 'оперативной памяти')
                elif sub_choice == '5':
                    logic.deleting_part('ссд', 'ссд')
                elif sub_choice == '0':
                    deleting = False
                else:
                    print('\nПожалуйста, введите правильный номер!')

        elif main_choice == '0':
            print(' 👋 До свидания!')
            break

        else:
            print('Пожалуйста, введите правильную команду.')

logic.load_data()
logic.load_build()
main_menu()
logic.save_data()