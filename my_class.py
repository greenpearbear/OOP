from abc import abstractmethod


class Storage:

    @abstractmethod
    def add(self, title, count):
        pass

    @abstractmethod
    def remove(self, title, count):
        pass

    @abstractmethod
    def get_free_space(self):
        pass

    @abstractmethod
    def get_items(self):
        pass

    @abstractmethod
    def get_unique_items_count(self):
        pass


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, title, count):
        search_title = False
        if self.get_free_space >= count:
            for key in self._items.keys():
                if title == key:
                    self._items[key] += count
                    search_title = True
            if not search_title:
                self._items[title] = count
            print('Товар добавлен')
        else:
            if self.get_free_space != 0:
                print(f'Товар не может быть добавлен, места хватит только на {self.get_free_space}')
            else:
                print('Товар не может быть добавлен, места нет')

    def remove(self, title, count):
        search_title = False
        for key in self._items.keys():
            if title == key:
                search_title = True
                if self._items[key] - count >= 0:
                    self._items[key] = self._items[key] - count
                else:
                    print(f'Слишком мало {title}')
        if not search_title:
            print(f'На складе нет {title}')

    @property
    def get_item(self):
        return self._items

    @property
    def get_free_space(self):
        return self._capacity - sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())


class Shop(Store):
    def __init__(self, limit=5):
        super().__init__()
        self._items = {}
        self._capacity = 20
        self._limit = limit

    @property
    def get_item_limit(self):
        return self._limit

    @property
    def capacity(self):
        return self._capacity

    def add(self, title, count):
        if self.get_unique_items_count <= self._limit:
            super().add(title, count)
        else:
            print('Слишком много разных товаров')


class Request:
    def __init__(self, string):
        str_to_list = self.str_to_list(string)

        self._from = str_to_list[4]
        self._count = int(str_to_list[1])
        self._product = str_to_list[2]
        self._to = str_to_list[6]

    def str_to_list(self, string):
        return string.split(' ')

    @property
    def count(self):
        return self._count

    @property
    def product(self):
        return self._product

    def __repr__(self):
        return f'Доставить {self._count} {self._product} из {self._from} в {self._to}'
