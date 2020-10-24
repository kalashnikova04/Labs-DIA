from operator import itemgetter


class HDD:
    """Жесткий диск"""

    def __init__(self, id, name, capacity, price, comp_id):
        self.id = id
        self.name = name
        self.capacity = capacity
        self.price = price
        self.comp_id = comp_id


class Cmp:
    """Компьютер"""

    def __init__(self, id, model):
        self.id = id
        self.model = model


class CmpHDD:
    """
    'Жесткие диски компьютеров' для реализации
    связи многие-ко-многим
    """

    def __init__(self, comp_id, hdd_id):
        self.comp_id = comp_id
        self.hdd_id = hdd_id


# Компьютеры
computers = [
    Cmp(1, 'Apple'),
    Cmp(2, 'Acer'),
    Cmp(3, 'Asus'),

    Cmp(11, 'Dell'),
    Cmp(22, 'Lenovo'),
    Cmp(33, 'hp'),
]

# Жесткие диски
hdds = [
    HDD(1, 'Aeagate', '256GB', 1790, 1),
    HDD(2, 'Toshiba', '1TB', 3200, 2),
    HDD(3, 'Samsung', '2TB', 6100, 22),

    HDD(4, 'WD', '1TB', 3290, 3),
    HDD(5, 'Toshiba', '512GB', 2500, 11),
    HDD(6, 'Fujitsu', '128GB', 1110, 33),
]

comps_hdds = [
    CmpHDD(1, 1),
    CmpHDD(2, 2),
    CmpHDD(3, 3),
    CmpHDD(3, 4),
    CmpHDD(3, 5),

    CmpHDD(11, 1),
    CmpHDD(22, 2),
    CmpHDD(33, 3),
    CmpHDD(33, 4),
    CmpHDD(33, 5),
]


def main():
    """Основная функция"""

    # Соединение данных один-ко-многим
    one_to_many = [(h.name, h.capacity, h.price, c.model)
                   for c in computers
                   for h in hdds
                   if h.comp_id == c.id]

    # Соединение данных многие-ко-многим
    many_to_many_temp = [(c.model, ch.comp_id, ch.hdd_id)
                         for c in computers
                         for ch in comps_hdds
                         if c.id == ch.comp_id]

    many_to_many = [(h.name, h.capacity, h.price, comp_model)
                    for comp_model, comp_id, hdd_id in many_to_many_temp
                    for h in hdds if h.id == hdd_id]

    print('Задание А1')
    res_11 = list(filter(lambda x: x[3].startswith('А'), one_to_many))
    print(res_11)

    print('\nЗадание А2')
    res_12_unsorted = []
    # Перебираем все компьютеры
    for c in computers:
        # Список жестких дисков
        c_hdds = list(filter(lambda i: i[3] == c.model, one_to_many))
        # Если есть компьютер
        if len(c_hdds) > 0:
            # Стоимость
            c_prices = [price for _, _, price, _ in c_hdds]
            # Максимальная стоимость жестких дисков
            c_prices_max = max(c_prices)
            res_12_unsorted.append((c.model, c_prices_max))

    # Сортировка по max стоимости
    res_12 = sorted(res_12_unsorted, key=itemgetter(1), reverse=True)
    for i in res_12:
        print(i)


    print('\nЗадание А3')
    res_13 = sorted(many_to_many, key=itemgetter(3))
    for i in res_13:
        print(i)


if __name__ == '__main__':
    main()
