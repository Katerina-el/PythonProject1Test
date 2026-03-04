import json

with open("Module20.txt", "r") as test_file:
    test_data = json.load(test_file)

#1. Какой номер самого дорого заказа за июль
max_price = 0
max_order_number = []

for order_number, order_data in test_data.items():
    if '2023-01-07' <= order_data['date'] <= '2023-31-07':
        if order_data['price'] > max_price:
            max_price = order_data['price']
            max_order_number = [order_number]
        elif order_data['price'] == max_price:
            max_order_number.append(order_number)
print(f'Номер заказа с самой большой стоимостью: {max_order_number}, стоимость заказа: {max_price}')
print()

#2. Какой номер заказа с самым большим количеством товаров?
max_count = 0
max_order_number = []
for order_number, order_data in test_data.items():
    if '2023-01-07' <= order_data['date'] <= '2023-31-07':
        if order_data['quantity'] > max_count:
            max_count = order_data['quantity']
            max_order_number = [order_number]
        elif order_data['quantity'] == max_count:
            max_order_number.append(order_number)
print(f'Номер заказа с самым большим количеством товаров: {max_order_number}, количество товаров: {max_count}')
print()

#3. В какой день в июле было сделано больше всего заказов
counts = {}
max_order = 0
day = []
for order_number, order_data in test_data.items():
    if '2023-01-07' <= order_data['date'] <= '2023-31-07':
        if order_data['date'] in counts:
            counts[order_data['date']] += 1
        else:
            counts[order_data['date']] = 1

if counts:
    first_day = list(counts.keys())[0]
    reference_day = counts[first_day]

    if_bool = True
    for daycount in counts:
        if counts[daycount] != reference_day:
            if_bool = False

    if not if_bool:
        for daycount in counts:
            if counts[daycount] > max_order:
                max_order = counts[daycount]
                day = [daycount]
            elif counts[daycount] == max_order:
                day.append(daycount)
        print(f'{day} было сделано больше всего заказов, их количество: {max_order}')
    else:
        print(f'Каждый день было сделано по {reference_day} заказу')
print()

#4. Какой пользователь сделал самое большое количество заказов за июль?
users = {}
max_user_count = 0
user = []
for order_number, order_data in test_data.items():
    if '2023-01-07' <= order_data['date'] <= '2023-31-07':
        if order_data['user_id'] in users:
            users[order_data['user_id']] += 1
        else:
            users[order_data['user_id']] = 1

if users:
    first_user_id = list(users.keys())[0]
    reference_count = users[first_user_id]

    if_bool = True
    for uid in users:
        if users[uid] != reference_count:
            if_bool = False

    if not if_bool:
        for uid in users:
            if users[uid] > max_user_count:
                max_user_count = users[uid]
                user = [uid]
            elif users[uid] == max_user_count:
                user.append(uid)
        print(f'Пользователь {user} сделал больше всего заказов: {max_user_count}')
    else:
        print(f'Каждый пользователь сделал по {reference_count} заказу')
print()

#5. У какого пользователя самая большая суммарная стоимость заказов за июль
users_price = {}
max_user_price = 0
user_price = []
for order_number, order_data in test_data.items():
    if '2023-01-07' <= order_data['date'] <= '2023-31-07':
        if order_data['user_id'] in users_price:
            users_price[order_data['user_id']] += order_data['price']
        else:
            users_price[order_data['user_id']] = order_data['price']

if users_price:
    first_user_id = list(users_price.keys())[0]
    reference_price = users_price[first_user_id]

    if_bool = True
    for uid in users_price:
        if users_price[uid] != reference_price:
            if_bool = False

    if not if_bool:
        for uid in users_price:
            if users_price[uid] > max_user_price:
                max_user_price = users_price[uid]
                user_price = [uid]
            elif users_price[uid] == max_user_price:
                user_price.append(uid)
        print(f'Пользователь {user_price} сделал больше всего заказов по стоимости: {max_user_price}')
    else:
        print(f'Каждый пользователь сделал заказы по стоимости {reference_price}')
print()

#6. Какая средняя стоимость заказа была в июле?
avg_price = 0
price = 0
count = 0
for order_number, order_data in test_data.items():
    if '2023-01-07' <= order_data['date'] <= '2023-31-07':
        price += order_data['price']
        count += 1
if count > 0:
    avg_price = round(price / count, 2)
    print(f"Средняя стоимость заказа: {avg_price}")
else:
    print(f'Заказов за июль не найдено')
print()

#7. Какая средняя стоимость товаров в июле?
avg_price_product = 0
price_product = 0
count_product = 0
for order_number, order_data in test_data.items():
    if '2023-01-07' <= order_data['date'] <= '2023-31-07':
        price_product += order_data['price'] / order_data['quantity']
        count_product += 1
if count_product > 0:
    avg_price_product = round(price_product / count_product, 2)
    print(f'Средняя стоимость товаров: {avg_price_product}')
else:
    print(f'Заказов за июль не найдено')








