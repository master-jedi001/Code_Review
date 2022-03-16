class ShopCatalog:
    __catalog_id = 0
    # review: здесь мне кажется можно было бы еще завести список или словарь для хранения в нем каталогов (просто для
    # удобства, чтобы можно было их вытаскивать, если потребуется)

    def __init__(self, catalog_name):
        self.catalog_name = catalog_name
        ShopCatalog.__catalog_id += 1
        self.__catalog_id = ShopCatalog.__catalog_id
        self.product_range = dict()
    # review: здесь я бы сделал поле product_range приватным, просто чтобы извне нельзя было поменять содержимое словаря
    # без специальных для этого методов
    # review: для поля catalog я бы сделал property и setter, чтобы проверять название каталога на корректность

    def add_item_to_product_range(self, item, price):
        if type(item) == str and isinstance(price, (int, float)):
            self.product_range[item] = price
        else:
            raise ValueError('Invalid data types!')
    # review: это еще вроде и как метод изменения цены работает, потому что если в словаре уже есть товар с именем item,
    # а item - это одновременно и ключ словаря, то если добавить в словарь снова item, но уже с другой ценой, то у
    # item уже будет эта новая цена

    def delete_item_from_product_range(self, item):
        del self.product_range[item]
    # review: здесь, мне кажется, перед удалением товара из каталога стоит еще проверить, есть ли данный товар в
    # каталоге, может его там и нет

    def get_product_range(self):
        print(f"Following items are in a '{self.catalog_name}' catalog:")
        return self.product_range

    def get_catalog_info(self):
        print(' ID and catalog name:')
        return f'{self.__catalog_id}: {self.catalog_name}'
# review: методы класса ShopCatalog очень хорошие, единственно что, есть интересный вопрос, а если например, удалить
# товар из каталога, который до этого был помещен в корзину к пользователю, то что произойдет с этим товаром в корзине?


class ConsumerOrder:

    def __init__(self, consumer):
        self.consumer = consumer
        self.items_ordered = dict()
    # review: здесь я бы сделал поле items_order приватным, а для поля consumer сделал бы property и setter с проверками
    # review: поле consumer, если я правильно понял, по смыслу должно содержать объект класса Consumer. Но при создании
    # корзины я могу в поле consumer положить что угодно, и мне тогда создаться корзина для несуществующего пользователя
    # review: я бы предложил, например, проверять, что type(consumer) == Consumer

    def get_counsumer_info(self):
        print(f'This basket belongs to {self.consumer.name}')

    def order_item(self, item, catalog):
        if item in catalog.product_range:
            self.items_ordered[item] = catalog.product_range[item]
            print(f"{item} was added to {self.consumer.name}'s basket")
        else:
            raise ValueError(f'There is no {item} in a {catalog.catalog_name} catalog!')

    def delete_item_from_basket(self, item):
        if item in self.items_ordered:
            del self.items_ordered[item]
        else:
            raise ValueError(f'There is no {item} in a basket!')

    def get_consumer_orders(self):
        print(f'{self.consumer.name} ordered following items:')
        return self.items_ordered

    def get_total_price(self):
        print(' Total price:')
        return sum(self.items_ordered.values())
    # review: все остальные методы класса ConsumerOrder на мой взгляд написаны очень хорошо
