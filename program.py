import consumer
import admin
import catalog


# TESTING MY PROGRAM

# Создаем покупателя
simple_fellow = consumer.Consumer('Micky', 'Mouse')
simple_fellow.get_consumer_personal_info()                                      # Получаем персональную информацию о покупателе


# Создаем администратора
admin = admin.Administrator('Taz', 'Mania')
admin.get_admin_personal_info()                                                 # Получаем персональную информацию об админе


# Создаем список товаров для покупки
simple_fellow.shopping_list = consumer.ShoppingList()
simple_fellow.shopping_list.add_item_to_shopping_list('Milk')
simple_fellow.shopping_list.add_item_to_shopping_list('Bread')
simple_fellow.shopping_list.add_item_to_shopping_list('Pencil')
print(simple_fellow.shopping_list)


# Создаем первый каталог
catalog1 = catalog.ShopCatalog('See, buy, fly')
print(catalog1.get_catalog_info())

catalog1.add_item_to_product_range('Milk', 50)
catalog1.add_item_to_product_range('Sugar', 65.5)
catalog1.add_item_to_product_range('Salt', 35)
catalog1.add_item_to_product_range('Tea', 40)
catalog1.add_item_to_product_range('Pepper', 20)

print(catalog1.get_product_range())


# Создаем второй каталог

catalog2 = catalog.ShopCatalog('Gajets')
print(catalog2.get_catalog_info())

catalog2.add_item_to_product_range('Iphone', 500)
catalog2.add_item_to_product_range('Ipad', 650.50)
catalog2.add_item_to_product_range('Chromebook', 700)

print(catalog2.get_product_range())


# Создаем первую корзину для покупателя (его заказы (ордеры))
Micky_order1 = catalog.ConsumerOrder(simple_fellow)

Micky_order1.get_counsumer_info()                                                # Получаем персональную информацию обладателя корзины (покупающего товары)

Micky_order1.order_item('Milk', catalog1)                                        # Добавляем товар из каталога
Micky_order1.order_item('Sugar', catalog1)
Micky_order1.order_item('Tea', catalog1)
# Micky_order.order_item('Ipad', catalog1)

print(Micky_order1.get_consumer_orders())                                        # Получаем информацию о товарах в корзине

Micky_order1.get_total_price()

# Создаем вторую корзину для покупателя (его заказы (ордеры))
Micky_order2 = catalog.ConsumerOrder(simple_fellow)

Micky_order2.get_counsumer_info()                                                # Получаем персональную информацию обладателя корзины (покупающего товары)

Micky_order2.order_item('Iphone', catalog2)                                      # Добавляем товар из каталога
Micky_order2.order_item('Ipad', catalog2)
Micky_order2.order_item('Chromebook', catalog2)

# Получаем информацию о заказах покупателя
simple_fellow.items_bought([Micky_order1, Micky_order2])                         # Метод принимает в качестве аргументов заказы


# Пример реализации методов админа
layman = consumer.Consumer('Looney', 'Toon')
layman.shopping_list = consumer.ShoppingList()
layman.shopping_list.add_item_to_shopping_list('Laptop')
layman.shopping_list.add_item_to_shopping_list('Smartphone')

admin.track_consumers([simple_fellow, layman])
admin.track_catalogs([catalog1, catalog2])

# Есть одно замечание по поводу класса Shopping_List. Сам по себе класс реализован очень хорошо, но в совокупноси со
# всей программой я не совсем до конца понял, для чего он нужен. Что я имею ввиду: класс ShoppingList живет как бы
# своей отдельной жизнью, то есть когда создается администратор, покупатель, каталоги, корзины, то при добавлении
# товаров в корзину, добавляются только те товары, которые есть в каталоге, плюс у корзины есть свой покупатель, здесь
# все очень логично, все хорошо связано и работает, но также есть отдельный список товаров (ShoppingList), который, как
# мне показалось, не очень логично вписывается во всю схему. То есть в нем есть товары, которых может не быть в
# каталоге, которых может даже не быть в корзине покупателя (как например товары Pencil и Bred из примера). То есть не очень
# понятно, что это за список товаров и для чего он вообще нужен. Если это список товаров, которые заказывал покупатель,
# то по идее он должен коррелировать с тем, что есть в корзине (product_range). Я бы здесь сделал немного по другому.
# Можно например было вообще убрать поле shopping_list у покупателя и сделать например в классе ConsumerOrder словарь
# или список, в котором бы хранились все корзины с товарами, и переделать метод track_consumers, потому что сейчас он
# выводит товары из shopping_list, в котором хранится не то же самое, что в корзинах покупателей. Наверное можно даже
# предложить еще что-то получше, чем предлагаю я, просто это пока первое, что приходит в голову. Но вполне возможно, что
# я просто что-то не допонял о классе ShoppingList и где-то и не прав.
# В целом мне реализация понравилось, все сделано очень логично и хорошо. Понравилась идея с хранением товаров в
# виде ключей словаря без создания отдельного класса товар
