1.Скачайте проект :)
2.Установите пакеты
3.Запустите

Для запуска выполните:
python duckshop_project/manage.py runserver

Использованные пакеты:
django = "5.1.4"
django-phone-field = "1.8.1"
crispy-bootstrap5 = "2024.10"
pillow = "11.0.0"

Архитектура:
    duckshop_project/users приложение кастомного пользователя
    duckshop_project/pages приложение магазина(все функции взаимодействия с товарами, корзиной и заказы)
    duckshop_project/templates шаблоны страниц проекта
    duckshop_project/media/images изображения используемые на страницах(сохраняются сюда при создании или изменении продукта)


Базовый обзор функций(на страницах найдёте больше интуитивно понятных кнопок):
    http://127.0.0.1:8000 - домашняя страница содержащая товары
    http://127.0.0.1:8000/cart/ - корзина
    1. При добавлении уже существующего товара количество складывается
    2. Кнопка "Order" удаляет записи из корзины и добавляет в таблицу "OrderEntry"(хранит детали заказа) попутно создав запись в таблице "Order"(все заказы)
    3. Кнопка "Edit quantity" перезаписывет значение количества

Аккаунты:
    Admin:
    Username: Supercrazy
    password: RootAdmin123
    User:
    Username: Testuser1
    password: Resume321

Скрытые ссылки(доступны только пользователям с permission add):
    http://127.0.0.1:8000/adminlist/ содержит страницу для создания и изменения продуктов
    http://127.0.0.1:8000/order/ содержит список всех заказов