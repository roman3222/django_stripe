# Django Stripe Payment Integration

Это Django-приложение, интегрирующее платежи через Stripe.

## Установка

1. Склонируйте репозиторий:

    ```bash
    git clone https://github.com/ваш-логин/django-stripe-payment.git
    cd django-stripe-payment
    ```

2. Создайте виртуальное окружение:

    ```bash
    python -m venv venv
    ```

3. Активируйте виртуальное окружение:

    - Для Windows:

        ```bash
        venv\Scripts\activate
        ```

    - Для macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Установите зависимости:

    ```bash
    pip install -r requirements.txt
    ```

5. Примените миграции:

    ```bash
    python manage.py migrate
    ```

6. Создайте суперпользователя:

    ```bash
    python manage.py createsuperuser
    ```

7. Запустите сервер:

    ```bash
    python manage.py runserver
    ```

8. Откройте приложение в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Stripe
- Документация https://stripe.com/docs

## Использование

- Добавьте товары, заказы, скидки, налоги через админ-панель Django.
- Перейдите в раздел покупок по URL
- Выберите товар и перейдите к оформлению заказа.
- Завершите оплату с использованием Stripe.


## Дополнительные настройки

- Настройте переменные окружения в файле `.env`:

    ```
    STRIPE_PUBLIC_KEY=your_stripe_public_key
    STRIPE_SECRET_KEY=your_stripe_secret_key
    db_name=your name database
    db_user=your user database
    db_password=password database
    db_port=port database
    db_host=host database
    SECRET_KEY=settings.py
    ALLOWED_HOSTS=settings.py
    DEBUG=settings.py
    ```

## Автор

Хопкин Роман
