# класс для создания покупателя
class Consumer:

    __consumer_id = 0
    __consumers = {}
    # review: хранить пользователей в словаре на мой взгляд очень классная идея

    def __init__(self, name, surname):
        Consumer.__consumer_id += 1
        self.__consumer_id = Consumer.__consumer_id
        self.name = name
        self.surname = surname
        self.shopping_list = None
        if self.name and self.surname:
            Consumer.__consumers[self.__consumer_id] = f'{self.name} {self.surname}'
    # review: здесь есть небольшие замечания: мне кажется не совсем удачно здесь использовать
    # условие (if self.name and self.surname). Если я правильно понял, это условие здесь стоит на тот случай,
    # если в поля name и surname будет введена пустая строка. Но тогда в этом случае объект все равно создатся, он не
    # попадет в словарь, но будет существовать и нигде не будет использоваться, что наверное не совсем хорошо
    # review: мне кажется, что было бы лучше убрать это условие, а вместо него делать дополнительную проверку в setter
    # и генерировать ошибку, если введена пустая строка. Но сама идея отслеживать, чтобы покупатели не оказались с
    # пустыми именами, очень классная
    # review: поле shopping_list я бы тоже сделал приватным (на всякий случай)

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        if type(name) == str:
            self.__name = name
        else:
            raise ValueError('Invalid data type!')

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, surname):
        if type(surname) == str:
            self.__surname = surname
        else:
            raise ValueError('Invalid data type!')
    # review: в сеттерах для фамилии и имени мне кажется лучше использовать регулярные выражения, тогда получится
    # охватить больше различных проверок

    def get_consumer_personal_info(self):
        print(' Consumer personal information:')
        print(f'{self.__consumer_id}: {self.name} {self.surname}')

    @classmethod
    def get_consumers(cls):
        return Consumer.__consumers

    def items_bought(self, consumer_orders):                                    # Отслеживание заказов и итоговой стоимости покупки
        for order in consumer_orders:
            print(f'{order.get_consumer_orders()}')
            print(f'{order.get_total_price()}')
    # review: если я правильно понял, то у одного покупателя может быть несколько корзин. Можно наверное еще добавить
    # метод по удаление корзины покупателя (не знаю только, куда его лучше добавить), а может и не надо :)

    # review: методы get_consumers и items_bought я бы сделал статическими (в items_bought убрал бы self, а над методом
    # написал бы  @staticmethod, в get_consumers я бы убрал cls, а вместо @classmethod написал бы @staticmethod, хотя
    # наверное get_consumers можно оставить и так, как сейчас есть). Но вообще сам метод items_bought для вывода
    # информации по всем корзинам пользователя, товарам в них и суммарным ценам очень хороший

    # review: еще один момент, на который я бы хотел обратить внимание. Сейчас класс Consumer позволяет создавать
    # дубликаты покупателей. То есть можно создать одного и того же покупателя несколько раз (хотя у инх конечно
    # будут разные id). Мне кажется тут можно было бы добавить поле phone, сделать проверку на корректность этого поля,
    # а также при создании нового покупателя по номеру телефона проверять, создан ли уже такой покупатель или нет. Но
    # реализация, которая есть сейчас, тоже очень хорошая


# Список товаров для покупки
class ShoppingList:

    def __init__(self):
        self.__items_to_buy = list()

    def __str__(self):
        print(" Consumer's shopping list:")
        return f'{self.__items_to_buy}'

    def add_item_to_shopping_list(self, item):                                   # Добавление наименования товара в список
        if item not in self.__items_to_buy:
            self.__items_to_buy.append(item)
        else:
            raise ValueError(f'{item} is already in a shopping list!')

    def delete_item_from_shopping_list(self, item):                              # Удаление наименования товара из списка
        if item in self.__items_to_buy:
            self.__items_to_buy.remove(item)
        else:
            raise ValueError(f'There is no {item} in a shopping list!')
# review: сам по себе класс Shopping_List реализован очень хорошо
# review: чуть подробнее свой комментарий об этом классе я оставил в program.py
