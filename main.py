import json
import os

database = {'видеокарты':{
    'nvidia': [],
    'amd': [],
    'intel': []
    },
    'процессоры':{
        'intel': [],
        'amd': []
    },
    'материнские_платы':{
        'msi': [],
        'asus': []
    },
    'оперативная_память':{
        'kingston': [],
        'g.skill': []
    },
    'ссд':{
        'samsung': [],
        'crucial': []
    }
}
data_to_save = {'видеокарты':{
    'nvidia': [],
    'amd': [],
    'intel': []
    },
    'процессоры':{
        'intel': [],
        'amd': []
    },'материнские_платы':{
        'msi': [],
        'asus': []
    },
    'оперативная_память':{
        'kingston': [],
        'g.skill': []
    },
    'ссд':{
        'samsung': [],
        'crucial': []
    }
}

pc_build = []

class Part:                                                      #version2.0
    def __init__(self,brand, name, price, verbose=True):
        self.brand = brand
        self.name = name
        self.price = price
        if verbose:
            print(f'Создана базовая деталь: {self.name}')

    def tell(self):
        print(f'Бренд: {self.brand} Модель: {self.name} Цена: {self.price}$', end = " ")

    def to_dict(self):
        return {
            'brand': self.brand,
            'name': self.name,
            'price': self.price,
        }

class GPU(Part):
    def __init__(self, brand, name, price, vram, interface, verbose=True):
        super().__init__(brand, name, price, verbose=verbose)
        self.vram = vram
        self.interface = interface

    def to_dict(self):
        d = super().to_dict()
        d.update({
                'vram': self.vram,
                'interface': self.interface
        })
        return d

    def tell(self):
        super().tell()
        print(f'Объём памяти: {self.vram}гб Интерфейс: {self.interface}')

class CPU(Part):
    def __init__(self, brand, name, price, cores, threads, socket, verbose=True):
        super().__init__(brand, name, price, verbose=verbose)
        self.cores = cores
        self.threads = threads
        self.socket = socket

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'cores': self.cores,
            'threads': self.threads,
            'socket': self.socket
        })
        return d

    def tell(self):
        super().tell()
        print(f'Ядер: {self.cores} Потоков: {self.threads} Сокет: {self.socket}')

class MBD(Part):
    def __init__(self, brand, name, price, chipset, form_factor, verbose=True):
        super().__init__(brand, name, price, verbose=verbose)
        self.chipset = chipset
        self.form_factor = form_factor

    def tell(self):
        super().tell()
        print(f'Чипсет: {self.chipset} Форм фактор: {self.form_factor}')

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'chipset': self.chipset,
            'form_factor': self.form_factor
        })
        return d

class RAM(Part):
    def __init__(self, brand, name, price, ram_type, frequency, memory, verbose=True):
        super().__init__(brand, name, price, verbose=verbose)
        self.ram_type = ram_type
        self.frequency = frequency
        self.memory = memory

    def tell(self):
        super().tell()
        print(f'Объём памяти: {self.memory}гб Тип: {self.ram_type} Частота: {self.frequency} МГц ')

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'ram_type': self.ram_type,
            'frequency': self.frequency,
            'memory': self.memory
        })
        return d

class SSD(Part):
    def __init__(self, brand, name, price, memory, speed, ssd_type, verbose=True):
        super().__init__(brand, name, price, verbose=verbose)
        self.memory = memory
        self.speed = speed
        self.ssd_type = ssd_type

    def tell(self):
        super().tell()
        print(f'Количество памяти:{self.memory}гб Скорость чтения: {self.speed}мб/сек Тип накопителя: {self.ssd_type}')

    def to_dict(self):
        d = super().to_dict()
        d.update({
            'memory': self.memory,
            'speed': self.speed,
            'ssd_type': self.ssd_type
        })
        return d


def save_data():
    for category in database:
        for brand in database[category]:
            data_to_save[category][brand].clear()
            for item in database[category][brand]:
                data_to_save[category][brand].append(item.to_dict())
    with open('hardware.json', 'w', encoding='utf-8') as f:
        json.dump(data_to_save, f, ensure_ascii=False, indent=4)
        print('\n[Система]: Данные успешно сохранены в hardware.json')


def load_data():
    filename = 'hardware.json'
    if not os.path.exists(filename):
        print('Файла нет, пропускаем загрузку...')
        return
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)

        for category in data:
            for brand in data[category]:
                for item in data[category][brand]:
                    if category == 'видеокарты':
                        obj = GPU(item['brand'], item['name'], item['price'], item['vram'], item['interface'],
                                  verbose=False)
                        database['видеокарты'][brand].append(obj)

                    elif category == 'процессоры':
                        obj = CPU(item['brand'], item['name'], item['price'], item['cores'], item['threads'],
                                  item['socket'], verbose=False)
                        database['процессоры'][brand].append(obj)

                    elif category == 'материнские_платы':
                        obj = MBD(item['brand'], item['name'], item['price'], item['chipset'], item['form_factor'], verbose=False)
                        database['материнские_платы'][brand].append(obj)

                    elif category == 'оперативная_память':
                        obj = RAM(item['brand'], item['name'], item['price'], item['ram_type'], item['frequency'], item['memory'], verbose=False)
                        database['оперативная_память'][brand].append(obj)

                    elif category == 'ссд':
                        obj = SSD(item['brand'], item['name'], item['price'], item['memory'], item['speed'], item['ssd_type'], verbose=False)
                        database['ссд'][brand].append(obj)



def main_menu():
    running = True
    while running:
        print('Что будете делать?')
        main_choice = input('добавить, удалить, сохранить,список, поиск или выход\n').lower()

        if main_choice == 'добавить' or main_choice == 'add':
            adding = True
            while adding:
                sub_choice = input('Введите: GPU, CPU, MBD, RAM или SSD: ').lower()
                if sub_choice == 'gpu':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['видеокарты']:
                        name = input('Введите модель: ')
                        while True:
                            try:
                                price = float(input('Введите цену: '))
                                vram = int(input('Введите количество vram: '))
                                break
                            except ValueError:
                                print('Ошибка! Вводите только цифры (например, 150 или 150.5')
                        interface = input('Введите интерфейс: ')
                        new_gpu = GPU(brand, name, price, vram, interface)
                        database['видеокарты'][brand].append(new_gpu)
                        save_data()
                        adding = False
                    else:
                        print(f'Ошибка, такого бренда "{brand}" нет в базе данных!')

                elif sub_choice == 'cpu':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['процессоры']:
                        name = input('Введите модель: ')
                        while True:
                            try:
                                price = float(input('Введите цену: '))
                                cores = int(input('Введите количество ядер: '))
                                threads = int(input('Введите количество потоков: '))
                                break
                            except ValueError:
                                print('Ошибка! Вводите только цифры (например, 150 или 150.5')
                        socket = input('Введите сокет: ')
                        new_cpu = CPU(brand, name, price, cores, threads, socket)
                        database['процессоры'][brand].append(new_cpu)
                        save_data()
                        adding = False
                    else:
                        print(f'Ошибка, такого бренда "{brand}" нет в базе данных!')

                elif sub_choice == 'mbd':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['материнские_платы']:
                        name = input('Введите модель: ')
                        while True:
                            try:
                                price = float(input('Введите цену: '))
                                break
                            except ValueError:
                                print('Ошибка! Вводите только цифры (например, 150 или 150.5')
                        chipset = input('Введите чипсет: ')
                        form_factor = input('Введите форм фактор: ')
                        new_mbd = MBD(brand, name, price, chipset, form_factor)
                        database['материнские_платы'][brand].append(new_mbd)
                        save_data()
                        adding = False
                    else:
                        print(f'Ошибка, такого бренда "{brand}" нет в базе данных!')

                elif sub_choice == 'ram':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['оперативная_память']:
                        name = input('Введите модель: ')
                        while True:
                            try:
                                price = float(input('Введите цену: '))
                                frequency = int(input('Введите частоту: '))
                                memory = int(input('Введите количество памяти: '))
                                break
                            except ValueError:
                                print('Ошибка! Вводите только цифры (например, 150 или 150.5')
                        ram_type = input("Введите тип памяти (прим. ddr4): ")
                        new_ram = RAM(brand, name, price, ram_type, frequency, memory)
                        database['оперативная_память'][brand].append(new_ram)
                        save_data()
                        adding = False
                    else:
                        print(f'Ошибка, такого бренда "{brand}" нет в базе данных!')

                elif sub_choice == 'ssd':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['ссд']:
                        name = input('Введите модель: ')
                        while True:
                            try:
                                price = float(input('Введите цену: '))
                                speed = int(input('Введите скорость: '))
                                memory = int(input('Введите количество памяти: '))
                                break
                            except ValueError:
                                print('Ошибка! Вводите только цифры (например, 150 или 150.5')
                        ssd_type = input("Введите тип ссд: ")
                        new_ssd = SSD(brand, name, price, memory, speed, ssd_type)
                        database['ссд'][brand].append(new_ssd)
                        save_data()
                        adding = False
                    else:
                        print(f'Ошибка, такого бренда "{brand}" нет в базе данных!')

                elif sub_choice == 'выход':
                    adding = False
                else:
                    print('Пожалуйста, введите правильное значение!')

        elif main_choice == 'удалить' or main_choice == 'del':
            deleting = True
            while deleting:
                sub_choice = input('Введите GPU, CPU, MBD, RAM, SSD или выход: ').lower()

                if sub_choice == 'gpu':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['видеокарты']:
                        name = input('Введите модель видеокарты: ')
                        found = False
                        for gpu in database['видеокарты'][brand]:
                            if gpu.name.lower() == name.lower():
                                database['видеокарты'][brand].remove(gpu)
                                save_data()
                                print(f'Модель {name} успешно удалена!')
                                found = True
                                break
                        if not found:
                            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"')

                elif sub_choice == 'cpu':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['процессоры']:
                        name = input('Введите модель процессора: ')
                        found = False
                        for cpu in database['процессоры'][brand]:
                            if cpu.name.lower() == name.lower():
                                database['процессоры'][brand].remove(cpu)
                                save_data()
                                print(f'Модель {name} успешно удалена!')
                                found = True
                                break
                        if not found:
                            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"')

                elif sub_choice == 'mbd':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['материнские_платы']:
                        name = input('Введите модель материнской платы: ')
                        found = False
                        for mbd in database['материнские_платы'][brand]:
                            if mbd.name.lower() == name.lower():
                                database['материнские_платы'][brand].remove(mbd)
                                save_data()
                                print(f'Модель {name} успешно удалена!')
                                found = True
                                break
                        if not found:
                            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"')

                elif sub_choice == 'ram':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['оперативная_память']:
                        name = input('Введите модель оперативной памяти: ')
                        found = False
                        for ram in database['оперативная_память'][brand]:
                            if ram.name.lower() == name.lower():
                                database['оперативная_память'][brand].remove(ram)
                                save_data()
                                print(f'Модель {name} успешно удалена!')
                                found = True
                                break
                        if not found:
                            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"')

                elif sub_choice == 'ssd':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['ссд']:
                        name = input('Введите модель ссд: ')
                        found = False
                        for ssd in database['ссд'][brand]:
                            if ssd.name.lower() == name.lower():
                                database['ссд'][brand].remove(ssd)
                                save_data()
                                print(f'Модель {name} успешно удалена!')
                                found = True
                                break
                        if not found:
                            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"')

                elif sub_choice == 'выход':
                    deleting = False
                else:
                    print('Пожалуйста, введите правильное значение!')
        elif main_choice == 'список':
            viewing = True
            while viewing:
                sub_choice = input('Введите gpu, cpu, mbd, ram, ssd, всё или выход: \n').lower()
                if sub_choice == 'gpu':
                    if any(database['видеокарты'].values()):
                        print("\n--- Список видеокарт ---")
                        for brand in database['видеокарты']:
                            for gpu in database['видеокарты'][brand]:
                                gpu.tell()
                        question = input('\nХотите что-то добавить в корзину? (да/нет)\n').lower()
                        if question == 'да':
                            choice = input('\nВведите желаемую модель: ')
                            found = False
                            for brand in database['видеокарты']:
                                for gpu in database['видеокарты'][brand]:
                                    if gpu.name.lower() == choice.lower():
                                        sub_choice = input('\nУверены в своём выборе? (да/нет) \n').lower()
                                        if sub_choice == 'да':
                                            pc_build.append(gpu)
                                            print('\nДеталь успешно добавлена в корзину\n')
                                            found = True
                                            break
                                        elif sub_choice == 'нет':
                                            print('\nТогда возвращаемся . . . \n')
                                            found = True
                                            break
                                        else:
                                            print('Пожалуйста, введите верное значение')
                                if found: break
                            if not found:
                                print(f'Модель "{choice}" не найдена в базе.')
                    else:
                        print('\n[Видеокарты:список пуст]')

                elif sub_choice == 'cpu':
                    if any(database['процессоры'].values()):
                        print("\n--- Список процессоров ---")
                        for brand in database['процессоры']:
                            for cpu in database['процессоры'][brand]:
                                cpu.tell()
                        question = input('\nХотите что-то добавить в корзину? (да/нет)\n').lower()
                        if question == 'да':
                            choice = input('\nВведите желаемую модель: ')
                            found = False
                            for brand in database['процессоры']:
                                for cpu in database['процессоры'][brand]:
                                    if cpu.name.lower() == choice.lower():
                                        sub_choice = input('\nУверены в своём выборе? (да/нет) \n').lower()
                                        if sub_choice == 'да':
                                            pc_build.append(cpu)
                                            print('\nДеталь успешно добавлена в корзину\n')
                                            found = True
                                            break
                                        elif sub_choice == 'нет':
                                            print('\nТогда возвращаемся . . . \n')
                                            found = True
                                            break
                                        else:
                                            print('Пожалуйста, введите верное значение')
                                if found: break
                            if not found:
                                print(f'Модель "{choice}" не найдена в базе.')
                    else:
                        print('\n[Процессоры: список пуст]')

                elif sub_choice == 'mbd':
                    if any(database['материнские_платы'].values()):
                        print("\n--- Список материнских плат ---")
                        for brand in database['материнские_платы']:
                            for mbd in database['материнские_платы'][brand]:
                                mbd.tell()
                        question = input('\nХотите что-то добавить в корзину? (да/нет)\n').lower()
                        if question == 'да':
                            choice = input('\nВведите желаемую модель: ')
                            found = False
                            for brand in database['материнские_платы']:
                                for mbd in database['материнские_платы'][brand]:
                                    if mbd.name.lower() == choice.lower():
                                        sub_choice = input('\nУверены в своём выборе? (да/нет) \n').lower()
                                        if sub_choice == 'да':
                                            pc_build.append(mbd)
                                            print('\nДеталь успешно добавлена в корзину\n')
                                            found = True
                                            break
                                        elif sub_choice == 'нет':
                                            print('\nТогда возвращаемся . . . \n')
                                            found = True
                                            break
                                        else:
                                            print('Пожалуйста, введите верное значение')
                                if found: break
                            if not found:
                                print(f'Модель "{choice}" не найдена в базе.')
                    else:
                        print('\n[Материнские платы: список пуст]')

                elif sub_choice == 'ram':
                    if any(database['оперативная_память'].values()):
                        print("\n--- Список оперативной памяти ---")
                        for brand in database['оперативная_память']:
                            for ram in database['оперативная_память'][brand]:
                                ram.tell()
                        question = input('\nХотите что-то добавить в корзину? (да/нет)\n').lower()
                        if question == 'да':
                            choice = input('\nВведите желаемую модель: ')
                            found = False
                            for brand in database['оперативная_память']:
                                for ram in database['оперативная_память'][brand]:
                                    if ram.name.lower() == choice.lower():
                                        sub_choice = input('\nУверены в своём выборе? (да/нет) \n').lower()
                                        if sub_choice == 'да':
                                            pc_build.append(ram)
                                            print('\nДеталь успешно добавлена в корзину\n')
                                            found = True
                                            break
                                        elif sub_choice == 'нет':
                                            print('\nТогда возвращаемся . . . \n')
                                            found = True
                                            break
                                        else:
                                            print('Пожалуйста, введите верное значение')
                                if found: break
                            if not found:
                                print(f'Модель "{choice}" не найдена в базе.')
                    else:
                        print('\n[Оперативная память: список пуст]')

                elif sub_choice == 'ssd':
                    if any(database['ссд'].values()):
                        print("\n--- Список SSD ---")
                        for brand in database['ссд']:
                            for ssd in database['ссд'][brand]:
                                ssd.tell()
                        question = input('\nХотите что-то добавить в корзину? (да/нет)\n').lower()
                        if question == 'да':
                            choice = input('\nВведите желаемую модель: ')
                            found = False
                            for brand in database['ссд']:
                                for ssd in database['ссд'][brand]:
                                    if ssd.name.lower() == choice.lower():
                                        sub_choice = input('\nУверены в своём выборе? (да/нет) \n').lower()
                                        if sub_choice == 'да':
                                            pc_build.append(ssd)
                                            print('\nДеталь успешно добавлена в корзину\n')
                                            found = True
                                            break
                                        elif sub_choice == 'нет':
                                            print('\nТогда возвращаемся . . . \n')
                                            found = True
                                            break
                                        else:
                                            print('Пожалуйста, введите верное значение')
                                if found: break
                            if not found:
                                print(f'Модель "{choice}" не найдена в базе.')
                    else:
                        print('\n[SSD: список пуст]')

                elif sub_choice == 'всё':
                    print("\n=== ВСЯ БАЗА КОМПЛЕКТУЮЩИХ ===")
                    print('\n---Видеокарты---')
                    if any(database['видеокарты'].values()):
                        for brand in database['видеокарты']:
                            for gpu in database['видеокарты'][brand]:
                                gpu.tell()
                    else:print('\n[Видеокарты:список пуст]')

                    print('\n---Процессоры---')
                    if any(database['процессоры'].values()):
                        for brand in database['процессоры']:
                            for cpu in database['процессоры'][brand]:
                                cpu.tell()
                    else:print('\n[Процессоры: список пуст]')

                    print("\n--- Список материнских плат ---")
                    if any(database['материнские_платы'].values()):
                        for brand in database['материнские_платы']:
                            for mbd in database['материнские_платы'][brand]:
                                mbd.tell()
                    else:
                        print('\n[Материнские платы: список пуст]')

                    print("\n--- Список оперативной памяти ---")
                    if any(database['оперативная_память'].values()):
                        for brand in database['оперативная_память']:
                            for ram in database['оперативная_память'][brand]:
                                ram.tell()
                    else:
                        print('\n[Оперативная память: список пуст]')

                    print("\n--- Список SSD ---")
                    if any(database['ссд'].values()):
                        for brand in database['ссд']:
                            for ssd in database['ссд'][brand]:
                                ssd.tell()
                    else:
                        print('\n[SSD: список пуст]')

                    total_price = 0
                    for category in database:
                        for brand in database[category]:
                            for item in database[category][brand]:
                                total_price += item.price
                    print(f"\n===============================")
                    print(f"ОБЩАЯ СТОИМОСТЬ ЖЕЛЕЗА В БАЗЕ: {total_price}$")
                    print(f"===============================")
                    question = input('\nХотите что-то добавить в корзину? (да/нет)\n').lower()
                    if question == 'да':
                        choice = input('\nВведите желаемую модель: ')
                        found = False
                        for category in database:
                            for brand in database[category]:
                                for item in database[category][brand]:
                                    if item.name.lower() == choice.lower():
                                        sub_choice = input('\nУверены в своём выборе? (да/нет) \n').lower()
                                        if sub_choice == 'да':
                                            pc_build.append(item)
                                            print('\nДеталь успешно добавлена в корзину\n')
                                            found = True
                                            break
                                        elif sub_choice == 'нет':
                                            print('\nТогда возвращаемся . . . \n')
                                            found = True
                                            break
                                        else:
                                            print('Пожалуйста, введите верное значение')
                                if found: break
                            if found: break
                        if not found:
                            print(f'Модель "{choice}" не найдена в базе.')


                elif sub_choice == 'выход':
                    viewing = False
                else:
                    print('Пожалуйста, введите верное значение!')

        elif main_choice == 'поиск':
            searching = True
            while searching:
                search = input('Поиск в GPU, CPU, MBD, RAM или SSD? +выход\n').lower()
                if search == 'gpu':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['видеокарты']:
                        name = input('Введите существующую модель ')
                        found = False
                        for gpu in database['видеокарты'][brand]:
                            if gpu.name.lower() == name.lower():
                                gpu.tell()
                                sub_choice = input('\nДобавить эту деталь в сборку? (да/нет) \n').lower()
                                if sub_choice == 'да':
                                    pc_build.append(gpu)
                                    print('\nДеталь успешно добавлена в корзину\n')
                                found = True
                                searching = False
                        if not found:
                            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"!')
                    else:
                        print(f'Ошибка! Такого бренда "{brand}" нет в базе!')

                elif search == 'cpu':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['процессоры']:
                        name = input('Введите существующую модель ')
                        found = False
                        for cpu in database['процессоры'][brand]:
                            if cpu.name.lower() == name.lower():
                                cpu.tell()
                                sub_choice = input('\nДобавить эту деталь в сборку? (да/нет) \n').lower()
                                if sub_choice == 'да':
                                    pc_build.append(cpu)
                                    print('\nДеталь успешно добавлена в корзину\n')
                                found = True
                                searching = False
                        if not found:
                            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"!')
                    else:
                        print(f'Ошибка! Такого бренда "{brand}" нет в базе!')

                elif search == 'mbd':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['материнские_платы']:
                        name = input('Введите существующую модель ')
                        found = False
                        for mbd in database['материнские_платы'][brand]:
                            if mbd.name.lower() == name.lower():
                                mbd.tell()
                                sub_choice = input('\nДобавить эту деталь в сборку? (да/нет) \n').lower()
                                if sub_choice == 'да':
                                    pc_build.append(mbd)
                                    print('\nДеталь успешно добавлена в корзину\n')
                                found = True
                                searching = False
                        if not found:
                            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"!')
                    else:
                        print(f'Ошибка! Такого бренда "{brand}" нет в базе!')

                elif search == 'ram':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['оперативная_память']:
                        name = input('Введите существующую модель ')
                        found = False
                        for ram in database['оперативная_память'][brand]:
                            if ram.name.lower() == name.lower():
                                ram.tell()
                                sub_choice = input('\nДобавить эту деталь в сборку? (да/нет) \n').lower()
                                if sub_choice == 'да':
                                    pc_build.append(ram)
                                    print('\nДеталь успешно добавлена в корзину\n')
                                found = True
                                searching = False
                        if not found:
                            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"!')
                    else:
                        print(f'Ошибка! Такого бренда "{brand}" нет в базе!')

                elif search == 'ssd':
                    brand = input('Введите бренд: ').lower()
                    if brand in database['ссд']:
                        name = input('Введите существующую модель ')
                        found = False
                        for ssd in database['ссд'][brand]:
                            if ssd.name.lower() == name.lower():
                                ssd.tell()
                                sub_choice = input('\nДобавить эту деталь в сборку? (да/нет) \n').lower()
                                if sub_choice == 'да':
                                    pc_build.append(ssd)
                                    print('\nДеталь успешно добавлена в корзину\n')
                                found = True
                                searching = False
                        if not found:
                            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"!')
                    else:
                        print(f'Ошибка! Такого бренда "{brand}" нет в базе!')

                elif search == 'выход':
                    print('Выходим...')
                    searching = False

                else:
                    print('Пожалуйста, введите верное значение')
        elif main_choice == 'сохранить':
            save_data()
            print('Данные успешно сохранены!')
        elif main_choice == 'выход':
            print('До свидания!')
            break
        else:
            print('Пожалуйста, введите правильную команду.')
load_data()
main_menu()
save_data()