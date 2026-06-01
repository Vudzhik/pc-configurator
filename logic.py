def add_item(database, category_name):
    print(f'\nХорошо, теперь введите бренд для {category_name}:')
    brand = input()

    if brand in database:
        print(f'\nВведите новую модель {category_name}:')
        model = input()
        database[brand].append(model)
        print(f'\nГотово! В список {brand} добавлена модель {model}')
        return False
    else:
        print(f'\nОшибка! Бренда "{brand}" нет в базе.')
        return True

def remove_item(database, category_name):
    print(f'\nХорошо, теперь введите бренд для {category_name}:')
    brand = input()

    if brand in database:
        print(f'\nВведите существующую модель {category_name}:')
        print(f'\nСейчас там {database[brand]}").')
        model = input()
        if model in database[brand]:
            database[brand].remove(model)
            print(f'\nГотово! Из списка {brand} убрана модель {model}')
            return False
        else:
            print(f'\nОшибка! Модели"{model}" нет в списке бренда {brand}')
            return True
    else:
        print(f'\nОшибка! Бренда {brand} нет в базе.')
        return True