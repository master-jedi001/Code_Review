import consumer
import catalog

class Administrator:

    __admin_id = 0
    # review: можно наверное еще словарь сделать, куда будут добавляться админы подобно тому, как в классе Consumer (но
    # это если считать, что их может быть несколько)

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        Administrator.__admin_id += 1
        self.__admin_id = Administrator.__admin_id

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
    # в полях имя и фамилия я бы тоже сделал дополнительные проверки на корректность заполнения этих полей (регулярныее
    # выражения, что поле - это не пустая строка, что одни и те же админы не создаются по нескольку раз и т.д.)

    def get_admin_personal_info(self):
        print(' Administrator personal information:')
        print(f'{self.__admin_id}: {self.name} {self.surname}')

    def track_consumers(self, consumers):
        print(' Information about consumers:')
        for consumer in consumers:
            consumer.get_consumer_personal_info()
            if consumer.shopping_list:
                print(consumer.shopping_list)
            print('')

    def track_catalogs(self, catalogs):
        print(' Information about catalogs and their product range:')
        for catalog in catalogs:
            print(catalog.get_catalog_info())
            print(catalog.product_range)
            print('')

    def add_item_to_catalog(self, item, price):
        if item and price:
            catalog.ShopCatalog.add_item_to_product_range(item, price)

    def delete_item_from_catalog(self, item):
        catalog.ShopCatalog.delete_item_from_product_range(item)

    # review: последние четыре метода я бы сделал статическими (добавил @staticmethod над названием каждого метода и
    # убрал бы self)

    # review: по поводу метода track_consumers есть небольшое замечание, связанное с классом ShoppingList (чуть
    # подробнее свой комментарий об этом классе я оставил в program.py)

    # review: замечание по поводу двух последних методов (add_item_to_catalog и delete_item_from_catalog)
    # catalog.ShopCatalog.add_item_to_product_range(item, price) Здесь можно словить ошибку, потому что такой вызов
    # метода был бы правильным, если бы метод add_item_to_product_range класса ShopCatalog был бы статическим, а он на
    # самом деле не статический. Этот метод принимает три аргумента, первый из которых - это каталог
    # (объект класса ShopCatalog). Поэтому правильнее будет сделать так:

    # @staticmethod
    # def add_item_to_catalog(item, price):
    #     catalog.ShopCatalog('See, buy, fly').add_item_to_product_range(item, price)

    # Но правда в этом случае создается каталог и потом в него добавляется товар. Или лучше наверное так (передать
    # первым аргументом каталог, в который нужно добавить товар):

    # @staticmethod
    # def add_item_to_catalog(catalog, item, price):
    #     catalog.add_item_to_product_range(item, price)

    # Аналогично с методом delete_item_from_catalog

    # review: с идейной точки зрения класс Admin реализован очень хорошо
