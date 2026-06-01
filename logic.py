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
        brand_aligned = self.brand.ljust(12)
        name_aligned = self.name.ljust(20)
        price_aligned = f"{self.price}$".ljust(8)

        print(f'Бренд: {brand_aligned} | Модель: {name_aligned} | Цена: {price_aligned} |', end=" ")

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
        vram_aligned = str(self.vram).ljust(2)
        interface_aligned = self.interface.ljust(14)
        print(f'Память: {vram_aligned}гб | Интерфейс: {interface_aligned} ')

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
        cores_aligned = str(self.cores).ljust(3)
        threads_aligned = str(self.threads).ljust(3)
        socket_aligned = self.socket.ljust(10)
        print(f'Ядер: {cores_aligned} | Потоков: {threads_aligned} | Сокет: {socket_aligned}')

class MBD(Part):
    def __init__(self, brand, name, price, chipset, form_factor, verbose=True):
        super().__init__(brand, name, price, verbose=verbose)
        self.chipset = chipset
        self.form_factor = form_factor

    def tell(self):
        super().tell()
        chipset_aligned = self.chipset.ljust(6)
        form_factor_aligned = self.form_factor.ljust(10)
        print(f'Чипсет: {chipset_aligned} | Форм фактор: {form_factor_aligned}')

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
        ram_type_aligned = self.ram_type.ljust(5)
        frequency_aligned = str(self.frequency).ljust(4)
        memory_aligned = str(self.memory).ljust(2)
        print(f'Память: {memory_aligned}гб | Тип: {ram_type_aligned} | Частота: {frequency_aligned} МГц ')

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
        memory_aligned = str(self.memory).ljust(5)
        speed_aligned = str(self.speed).ljust(5)
        ssd_type_aligned = str(self.ssd_type).ljust(5)
        print(f'Память: {memory_aligned}гб | Скорость: {speed_aligned}мб/сек | Тип: {ssd_type_aligned}')

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

def save_build():
    build_to_save = []
    for item in pc_build:
        item_dict = item.to_dict()
        if isinstance(item, GPU):
            item_dict['type'] = 'gpu'
        elif isinstance(item, CPU):
            item_dict['type'] = 'cpu'
        elif isinstance(item, MBD):
            item_dict['type'] = 'mbd'
        elif isinstance(item, RAM):
            item_dict['type'] = 'ram'
        elif isinstance(item, SSD):
            item_dict['type'] = 'ssd'
        build_to_save.append(item_dict)
    with open('user_build.json', 'w', encoding='utf-8') as f:
        json.dump(build_to_save, f, ensure_ascii=False, indent=4)
    print('\n[Система]: Сборка ПК успешно сохранена в файл user_build.json!')

def load_build():
    filename = 'user_build.json'
    if not os.path.exists(filename):
        return
    pc_build.clear()
    with open(filename, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
            for item in data:
                if item['type'] == 'gpu':
                    obj = GPU(item['brand'], item['name'], item['price'], item['vram'], item['interface'], verbose=False)
                elif item['type'] == 'cpu':
                    obj = CPU(item['brand'], item['name'], item['price'], item['cores'], item['threads'], item['socket'], verbose=False)
                elif item['type'] == 'mbd':
                    obj = MBD(item['brand'], item['name'], item['price'], item['chipset'], item['form_factor'], verbose=False)
                elif item['type'] == 'ram':
                    obj = RAM(item['brand'], item['name'], item['price'], item['ram_type'], item['frequency'], item['memory'], verbose=False)
                elif item['type'] == 'ssd':
                    obj = SSD(item['brand'], item['name'], item['price'], item['memory'], item['speed'], item['ssd_type'], verbose=False)
                pc_build.append(obj)
        except json.JSONDecodeError:
            print("[Система]: Ошибка чтения файла user_build.json. Файл поврежден.")

def deleting_part(category_key, item_name_ru):
    brand = input('Введите бренд: ').lower()
    if brand in database[category_key]:
        name = input(f'Введите модель {item_name_ru}: ').lower()
        found = False
        for item in database[category_key][brand]:
            if item.name.lower() == name.lower():
                database[category_key][brand].remove(item)
                save_data()
                print(f'Модель "{name}" успешно удалена!')
                found = True
                break
        if not found:
            print(f'Ошибка! Модель "{name}" не найдена в списке "{brand}"')
    else:
        print(f'Ошибка! Такого бренда "{brand}" нет в базе данных!')

def details_list(category_key, item_name_ru):
    if any(database[category_key].values()):
        print(f"\n--- Список {item_name_ru} ---")
        for brand in database[category_key]:
            for item in database[category_key][brand]:
                item.tell()
    else:
        print(f'\n[Список {item_name_ru} пуст]')

def get_int_input(название):
    while True:
        try:
            value = int(input(f'Введите {название}: \n'))
            return value
        except ValueError:
            print('Ошибка! Вводите только целые цифры.')

def global_search():
    choice = input(' 🔎 Введите название желаемой модели: \n').lower()
    found = False
    for category in database:
        for brand in database[category]:
            for item in database[category][brand]:
                if item.name.lower() == choice.lower():
                    item.tell()
                    while True:
                        print('--- Хотите добавить эту деталь в сборку? ---\n')
                        print(' [1] 📥 Добавить')
                        print(' [2] ⏩ Пропустить')
                        sub_choice = input('Выберите номер действия\n').strip()
                        if sub_choice == '1':
                            pc_build.append(item)
                            print('\n 📥 Деталь успешно добавлена в корзину\n')
                            found = True
                            break
                        elif sub_choice == '2':
                            print(' ⏩ Пропускаем...\n')
                            found = True
                            break
                        else:
                            print('\n 🚫 Пожалуйста, введите верное значение.\n')
                if found: break
            if found: break
        if found: break
    if not found:
        print(f'\n 🚫 Модель {choice} не найдена в базе.\n')

def user_build():
    print('\n-----Ваша сборка-----')
    total_price = 0
    for item in pc_build:
        item.tell()
        total_price += item.price
    print(f"\n===============================")
    print(f"Общая стоимость железа в сборке: {total_price}$")
    print(f"===============================")
    print('\n 🗑️ Хотите что-то убрать?')
    print(' [1] ✅ Да, уберите модель поскорее!')
    print(' [2] ❌ Нет, не хочу, верните меня в меню')
    print(' [3] 💥 Хочу щёлкнуть перчаткой Таноса (удалить всё)')
    sub_choice = input('\nВыберите номер действия').strip()
    if sub_choice == '1':
        name = input(f' 🔎 Введите название неугодной модели: ').lower()
        found = False
        for item in pc_build:
            if item.name.lower() == name.lower():
                pc_build.remove(item)
                save_build()
                print(f' 💥 Модель "{name}" успешно удалена из сборки!')
                found = True
                break
        if not found:
            print(f' 🚫 Ошибка! Модель "{name}" не найдена в вашей сборке')
    elif sub_choice == '3':
        print('Вы точно хотите удалить ВСЁ из корзины?')
        print(' [1] ✅ Да, и поскорее!')
        print(' [2] ❌ Нет, пощадите, я передумал')
        choice = input('Введите номер действия').strip()
        if choice == '1':
            pc_build.clear()
            save_build()
            print(' 💥 Вся ваша сборка успешно удалена!')

def adding(category_key_ru, brand_key, item_name, item_price):
    if category_key_ru in database:
        if brand_key in database[category_key_ru]:
            new_item = None

            if category_key_ru == 'видеокарты':
                vram = get_int_input('количество vram: ')
                interface = input('Введите интерфейс: ')
                new_item = GPU(brand_key, item_name, item_price, vram, interface)

            elif category_key_ru == 'процессоры':
                cores = get_int_input('количество ядер: ')
                threads = get_int_input('количество потоков: ')
                socket = input('Введите сокет: ')
                new_item = CPU(brand_key, item_name, item_price, cores, threads, socket)

            elif category_key_ru == 'материнские_платы':
                chipset = input('Введите чипсет: ')
                form_factor = input('Введите форм фактор: ')
                new_item = MBD(brand_key, item_name, item_price, chipset, form_factor)

            elif category_key_ru == 'оперативная_память':
                ram_type = input('Введите тип оперативной памяти: ')
                frequency = get_int_input('частоту: ')
                memory = get_int_input('количество памяти: ')
                new_item = RAM(brand_key, item_name, item_price, ram_type, frequency, memory)

            elif category_key_ru == 'ссд':
                memory = get_int_input('количество памяти: ')
                speed = get_int_input('скорость ссд: ')
                ssd_type = input('Введите тип ссд: ')
                new_item = SSD(brand_key, item_name, item_price, memory, speed, ssd_type)

            if new_item is not None:
                database[category_key_ru][brand_key].append(new_item)
                save_data()
                print('\nДеталь успешно добавлена в базу данных!\n')
        else:
            print(f'Ошибка! Такого бренда "{brand_key}" нет в категории "{category_key_ru}"!')
    else:
        print(f'Ошибка! Категории "{category_key_ru}" не существует!')

def add_question():
    print('--- Хотите что-то добавить в корзину? ---\n')
    print(' [1] 📥 Добавить')
    print(' [2] ⏩ Пропустить')
    question = input('Выберите номер действия\n').strip()
    if question == '1':
        choice = input('\nВведите название желаемой модели: ')
        found = False
        for category in database:
            for brand in database[category]:
                for item in database[category][brand]:
                    if item.name.lower() == choice.lower():
                        while True:
                            print('--- Уверены в своём выборе? ---\n')
                            print(' [1] 📥 Уверен, добавляйте ')
                            print(' [2] ⏩ Не уверен, возвращаемся')
                            sub_choice = input('Выберите номер действия\n').strip()
                            if sub_choice == '1':
                                pc_build.append(item)
                                print('Деталь успешно добавлена в корзину\n')
                                found = True
                                break
                            elif sub_choice == '2':
                                print('\nТогда возвращаемся . . . \n')
                                found = True
                                break
                            else:
                                print('Пожалуйста, введите верное значение')
                        if found: break
                if found: break
            if found: break
        if not found:
            print(f' 🚫 Ошибка! Модель "{choice}" не найдена в базе.')