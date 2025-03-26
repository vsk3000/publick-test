import json
from collections import defaultdict

# Чтение данных из файла
with open("orders_july_2023.json", "r") as file:
    orders = json.load(file)

# 1. Самый дорогой заказ
max_price = 0
max_price_order = None
for order_num, order_data in orders.items():
    if order_data['price'] > max_price:
        max_price = order_data['price']
        max_price_order = order_num

# 2. Заказ с наибольшим количеством товаров
max_quantity = 0
max_quantity_order = None
for order_num, order_data in orders.items():
    if order_data['quantity'] > max_quantity:
        max_quantity = order_data['quantity']
        max_quantity_order = order_num

# 3. День с наибольшим количеством заказов
date_counts = defaultdict(int)
for order_data in orders.values():
    date_counts[order_data['date']] += 1
busiest_day = max(date_counts, key=date_counts.get)

# 4. Пользователь с наибольшим количеством заказов
user_order_counts = defaultdict(int)
for order_data in orders.values():
    user_order_counts[order_data['user_id']] += 1
most_active_user = max(user_order_counts, key=user_order_counts.get)

# 5. Пользователь с наибольшей суммарной стоимостью заказов
user_total_spent = defaultdict(int)
for order_data in orders.values():
    user_total_spent[order_data['user_id']] += order_data['price']
biggest_spender = max(user_total_spent, key=user_total_spent.get)

# 6. Средняя стоимость заказа
total_orders = len(orders)
total_price = sum(order['price'] for order in orders.values())
average_order_price = total_price / total_orders

# 7. Средняя стоимость товара
total_items = sum(order['quantity'] for order in orders.values())
average_item_price = total_price / total_items