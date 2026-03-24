from app import app, db, User, Dish, Order, OrderItem, Booking
from datetime import datetime, timedelta


def seed_database():
    with app.app_context():
        db.drop_all()
        db.create_all()

        user1 = User(username='ivan_petrenko', email='ivan@example.com')
        user1.set_password('password123')
        db.session.add(user1)

        user2 = User(username='olena_kovalenko', email='olena@example.com')
        user2.set_password('password123')
        db.session.add(user2)

        # Всі photo ID перевірені через пошук Unsplash
        I = 'https://images.unsplash.com/photo-'

        dishes = [

            # ── ЗАКУСКИ ───────────────────────────────────────────────────
            Dish(name='Брускета аль Помодоро',
                 description='Підсмажений хліб зі свіжими помідорами, часником, базиліком та оливковою олією',
                 price=12.99, category='appetizers',
                 image_url=I+'1572695157366-5e585ab2b69f?w=600&q=80'),

            Dish(name='Кальмарі Фрітті',
                 description='Хрусткі кільця кальмара у фритюрі з лимоном та соусом марінара',
                 price=14.99, category='appetizers',
                 image_url='https://images.unsplash.com/photo-1599487488170-d11ec9c172f0?w=600&q=80'),

            Dish(name='Капрезе',
                 description='Класичний салат із моцарели буфало, стиглих помідорів та базиліку з бальзамічним кремом',
                 price=13.99, category='appetizers',
                 image_url=I+'1608897013039-887f21d8c804?w=600&q=80'),

            Dish(name='Карпаччо з яловичини',
                 description='Тонко нарізана яловичина з рукколою, пармезаном та трюфельною олією',
                 price=16.99, category='appetizers',
                 image_url=I+'1615361200141-f45040f367be?w=600&q=80'),

            Dish(name='Тартар із лосося',
                 description='Свіжий лосось з авокадо, каперсами, червоною цибулею та лимонним соусом',
                 price=17.99, category='appetizers',
                 image_url='https://images.unsplash.com/photo-1535473895227-bdecb20fb157?w=600&q=80'),

            Dish(name='Суп Мінестроне',
                 description='Густий овочевий суп із сезонних овочів, квасолі та пасти з пармезаном',
                 price=11.99, category='appetizers',
                 image_url=I+'1547592180-85f173990554?w=600&q=80'),

            Dish(name='Фокачча з розмарином',
                 description='Пухка домашня фокачча з морською сіллю, розмарином та оливковою олією',
                 price=8.99, category='appetizers',
                 image_url='https://images.unsplash.com/photo-1619535860434-ba1d8fa12536?w=600&q=80'),

            Dish(name='Креветки на грилі',
                 description='Тигрові креветки на грилі з часниковим маслом та лимонним соком',
                 price=19.99, category='appetizers',
                 image_url=I+'1565680018434-b513d5e5fd47?w=600&q=80'),

            # ── ОСНОВНІ СТРАВИ ────────────────────────────────────────────
            Dish(name='Спагеті Карбонара',
                 description='Класична римська паста з яйцями, панчетою та сиром Пекоріно Романо',
                 price=16.99, category='main',
                 image_url=I+'1612874742237-6526221588e3?w=600&q=80'),

            Dish(name='Лазанья Болоньєзе',
                 description='Шари пасти з м\'ясним соусом болоньєзе та ніжним бешамелем',
                 price=18.99, category='main',
                 image_url=I+'1574894709920-11b28e7367e3?w=600&q=80'),

            Dish(name='Оссо Буко',
                 description='Тушковані телячі голяшки з овочами та білим вином по-міланськи',
                 price=28.99, category='main',
                 image_url=I+'1544025162-d76694265947?w=600&q=80'),

            Dish(name='Різото з грибами',
                 description='Вершкове різото Арборіо з лісовими грибами та трюфельною олією',
                 price=19.99, category='main',
                 image_url=I+'1476124369491-e7addf5db371?w=600&q=80'),

            Dish(name='Піца Маргарита',
                 description='Класична піца з томатним соусом, моцарелою та базиліком',
                 price=15.99, category='main',
                 image_url=I+'1574071318508-1cdbab80d002?w=600&q=80'),

            Dish(name='Піца Діавола',
                 description='Гостра піца з салямі, перцем чилі, оливками та моцарелою',
                 price=17.99, category='main',
                 image_url=I+'1628840042765-356cda07504e?w=600&q=80'),

            Dish(name='Тальятелле з морепродуктами',
                 description='Паста тальятелле з мідіями, кальмарами та креветками',
                 price=22.99, category='main',
                 image_url=I+'1563379926898-05f4575a45d8?w=600&q=80'),

            Dish(name='Стейк Флорентіно',
                 description='Яловичий стейк на деревному вугіллі з розмарином та часником',
                 price=34.99, category='main',
                 image_url=I+'1546833999-b9f581a1996d?w=600&q=80'),

            Dish(name='Феттучіне Альфредо',
                 description='Паста феттучіне у вершковому соусі з пармезаном та трюфелем',
                 price=20.99, category='main',
                 image_url=I+'1621996346565-e3dbc646d9a9?w=600&q=80'),

            Dish(name='Рибне філе на грилі',
                 description='Філе сибасу на грилі з лимонно-масляним соусом та каперсами',
                 price=24.99, category='main',
                 image_url=I+'1519708227418-c8fd9a32b7a2?w=600&q=80'),

            Dish(name='Пенне Арабіата',
                 description='Паста пенне в гострому томатному соусі з часником та чилі',
                 price=14.99, category='main',
                 image_url='https://images.unsplash.com/photo-1598866594230-a7c12756260f?w=600&q=80'),

            Dish(name='Курка Сальтімбокка',
                 description='Куряче філе з прошуто та шавлією у вершковому соусі по-римськи',
                 price=21.99, category='main',
                 image_url=I+'1604908176997-125f25cc6f3d?w=600&q=80'),

            # ── ДЕСЕРТИ ───────────────────────────────────────────────────
            Dish(name='Тірамісу',
                 description='Класичний десерт із маскарпоне, савоярді просочених еспресо та амаретто',
                 price=8.99, category='desserts',
                 image_url=I+'1571877227200-a0d98ea607e9?w=600&q=80'),

            Dish(name='Панна Котта',
                 description='Ніжний ванільний вершковий крем із соусом із лісових ягід',
                 price=7.99, category='desserts',
                 image_url=I+'1488477181946-6428a0291777?w=600&q=80'),

            Dish(name='Шоколадний фондан',
                 description='Теплий шоколадний кекс із рідкою начинкою з ванільним морозивом',
                 price=9.99, category='desserts',
                 image_url=I+'1606313564200-e75d5e30476c?w=600&q=80'),

            Dish(name='Чізкейк Нью-Йорк',
                 description='Вершковий чізкейк на пісочній основі з соусом із полуниці',
                 price=8.99, category='desserts',
                 image_url=I+'1565958011703-44f9829ba187?w=600&q=80'),

            Dish(name='Джелато Мікс',
                 description='Три кульки домашнього морозива: ваніль, фісташки або полуниця',
                 price=6.99, category='desserts',
                 image_url=I+'1570197788417-0e82375c9371?w=600&q=80'),

            Dish(name='Каннолі Сіціліані',
                 description='Хрусткі трубочки з рикотою та шоколадними краплями по-сицилійськи',
                 price=7.99, category='desserts',
                 image_url=I+'1551024506-0bccd828d307?w=600&q=80'),

            # ── НАПОЇ ─────────────────────────────────────────────────────
            Dish(name='Еспресо',
                 description='Міцна італійська кава із зерен арабіки з насиченим ароматом',
                 price=3.99, category='drinks',
                 image_url=I+'1510591509098-f4fdc6d0ff04?w=600&q=80'),

            Dish(name='Капучіно',
                 description='Класичний капучіно з еспресо, парного молока та молочної піни',
                 price=4.99, category='drinks',
                 image_url=I+'1572442388796-11668a67e53d?w=600&q=80'),

            Dish(name='Просекко',
                 description='Ігристе вино DOC з Венето з фруктовими та квітковими нотками',
                 price=9.99, category='drinks',
                 image_url=I+'1551024709-8f23befc6f87?w=600&q=80'),

            Dish(name='Кьянті Класіко',
                 description='Сухе червоне вино DOCG з Тоскани з нотками вишні та фіалки',
                 price=12.99, category='drinks',
                 image_url=I+'1510812431401-41d2bd2722f3?w=600&q=80'),

            Dish(name='Апероль Шпріц',
                 description='Ігристий аперитив із Апероля, Просекко та содової з апельсином',
                 price=8.99, category='drinks',
                 image_url='https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?w=600&q=80'),

            Dish(name='Лимонад Сіцілійський',
                 description='Домашній лимонад із сицилійських лимонів з м\'ятою та льодом',
                 price=5.99, category='drinks',
                 image_url=I+'1621263764928-df1444c5e859?w=600&q=80'),

            Dish(name='Лате Макіато',
                 description='Кавовий напій із парного молока та шару еспресо в склянці',
                 price=5.49, category='drinks',
                 image_url=I+'1561047029-3000c68339ca?w=600&q=80'),

            Dish(name='Мохіто Без Алкоголю',
                 description='Безалкогольний мохіто з м\'ятою, лаймом та тростинним цукром',
                 price=5.99, category='drinks',
                 image_url=I+'1551538827-9c037cb4f32a?w=600&q=80'),
        ]

        db.session.add_all(dishes)
        db.session.commit()

        order1 = Order(user_id=user1.id, total_price=42.97, status='confirmed')
        db.session.add(order1)
        db.session.flush()
        item1 = OrderItem(order_id=order1.id, dish_id=dishes[8].id, quantity=2, price=16.99)
        item2 = OrderItem(order_id=order1.id, dish_id=dishes[20].id, quantity=1, price=8.99)
        db.session.add_all([item1, item2])

        booking1 = Booking(
            user_id=user2.id,
            booking_date=datetime.utcnow() + timedelta(days=7),
            guests=4, status='confirmed',
            notes='Бажано столик біля вікна'
        )
        db.session.add(booking1)
        db.session.commit()

        cats = {}
        for d in dishes:
            cats[d.category] = cats.get(d.category, 0) + 1
        print(f'✅ База заповнена! Страв: {len(dishes)}')
        for cat, cnt in cats.items():
            print(f'   {cat}: {cnt}')


if __name__ == '__main__':
    seed_database()