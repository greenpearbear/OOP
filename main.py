from my_class import *

if __name__ == '__main__':
    store = Store()
    store.add('Яблоки', 5)
    store.add('Груши', 7)
    store.add('Пчелы', 10)
    shop = Shop()
    shop.add('Яблоки', 1)
    shop.add('Груши', 2)
    shop.add('Пчелы', 3)

    user_string = input('Введите строку по примеру\n'
                        'Доставить 3 печеньки из склад в магазин\n')

    string_Request = Request(user_string)

    if string_Request.product in store.get_item:
        if string_Request.count <= store.get_item[string_Request.product]:
            print('Нужное количество есть на складе')
            print(f'Курьер забрал {string_Request.count} {string_Request.product} со склад')
            print(f'Курьер везет {string_Request.count} {string_Request.product} со склад в магазин')
            if sum(shop.get_item.values()) + string_Request.count <= shop.capacity:
                print(f'Курьер доставил {string_Request.count} {string_Request.product} в магазин')
                store.remove(string_Request.product, string_Request.count)
                shop.add(string_Request.product, string_Request.count)
            else:
                print('В магазине недостаточно места')
        else:
            print('На складе не хватает товара')
    else:
        print('Товара нет на складе')

    print('В склад хранится')
    for key, value in store.get_item.items():
        print(key, value)

    print('В магазин хранится')
    for key, value in shop.get_item.items():
        print(key, value)
