from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import insert
from database.database import session_factory
from database.models import AccountCategoryORM, AccountProductORM

# Пример данных
accounts_data = {
    "Latam air": [
        "200k with cash | 150$",
        "30k with email | 20$",
        "10k with email | 10$"
    ],
    "Azul air": [
        "20k with email | 20$"
    ],
    "Delta": [
        "14k | 20$",
        "10k with email | 15$",
        "45k changed email | 25$",
        "40k with email | 25$"
    ],
    "IHG": [
        "15k | 20$",
        "13k with email | 15$"
    ],
    "Virgin Atlantic": [
        "38k with email | 40$"
    ],
    "Southwest": [
        "8k with credits 300$ without email | 150$"
    ],
    "Emirates": [
        "10k | 15$",
        "8k family with email | 10$"
    ],
    "Choice priviledge hotels": [
        "14k with email | 15$",
        "10k with email | 10$"
    ],
    "Singapore air": [
        "13k with email | 15$",
        "19k with email | 25$"
    ],
    "Hawaiian airlines": [
        "64k with email | 40$",
        "10k with email | 10$"
    ],
    "Iberia": [
        "25k with email 40$",
    ],
    "Turkish Airlines": [
        "28k with email 30$"
    ],
    "Hilton": [
        "Hilton 11k with email 10$",
        "Hilton 23k with email 10$"
    ]
}

async def seed_accounts():
    async with session_factory() as session:  # type: AsyncSession
        for category_name, product_list in accounts_data.items():
            # Создаем категорию
            category = AccountCategoryORM(name=category_name)
            session.add(category)
            await session.flush()  # Получаем ID категории до коммита

            # Добавляем товары
            for product_name in product_list:
                product = AccountProductORM(
                    name=product_name,
                    category_id=category.id
                )
                session.add(product)

        await session.commit()
        print("✅ Категории и продукты успешно добавлены.")
