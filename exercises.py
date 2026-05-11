# Корзина магазина
orders = {
    1: {
        'table': 1,
        'items': [
            {'name': 'Бургер', 'price': 350, 'quantity': 2},
            {'name': 'Кола', 'price': 150, 'quantity': 3},
        ]
    },
    2: {
        'table': 2,
        'items': [
            {'name': 'Пицца', 'price': 600, 'quantity': 1},
            {'name': 'Сок', 'price': 200, 'quantity': 2},
        ]
    },
    3: {
        'table': 1,
        'items': [
            {'name': 'Салат', 'price': 280, 'quantity': 1},
            {'name': 'Кола', 'price': 150, 'quantity': 2},
        ]
    }
}

def get_popular_item() -> str:
    result = ""
    dishes_quantity = dict()
    for order in orders.values():
        for value in order["items"]:
            if value["name"] in dishes_quantity:
                dishes_quantity[value["name"]] += value["quantity"]
            else:
                dishes_quantity[value["name"]] = value["quantity"]

    max_value = max(dishes_quantity.values())

    for key, value in dishes_quantity.items():
        if value == max_value:
            result = key
    return result


print(get_popular_item())
"""
Напиши функцию get_most_popular_item() -> str
Функция должна:

Посчитать суммарное количество (quantity) каждого блюда по всем заказам
Вернуть название блюда с наибольшим quantity
"""