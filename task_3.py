import csv
import os


def create_initial_csv():

    products = [
        ["Название", "Цена", "Количество"],
        ["Яблоки", "100", "50"],
        ["Бананы", "80", "30"],
        ["Молоко", "120", "20"],
        ["Хлеб", "40", "100"]
    ]

    with open('products.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(products)

    print("Файл products.csv успешно создан!")


def read_products():

    products = []
    try:
        with open('products.csv', 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                products.append({
                    'Название': row['Название'],
                    'Цена': int(row['Цена']),
                    'Количество': int(row['Количество'])
                })
    except FileNotFoundError:
        print("Файл products.csv не найден!")
        return []

    return products


def save_products(products):

    with open('products.csv', 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['Название', 'Цена', 'Количество']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(products)

    print("Данные успешно сохранены!")


def add_product(products):

    print("\n--- Добавление нового товара ---")
    name = input("Введите название товара: ").strip()

    for product in products:
        if product['Название'].lower() == name.lower():
            print("Товар с таким названием уже существует!")
            return

    try:
        price = int(input("Введите цену товара: "))
        quantity = int(input("Введите количество товара: "))

        products.append({
            'Название': name,
            'Цена': price,
            'Количество': quantity
        })
        print(f"Товар '{name}' успешно добавлен!")
    except ValueError:
        print("Ошибка: цена и количество должны быть числами!")


def search_product(products):

    print("\n--- Поиск товара ---")
    search_name = input("Введите название товара для поиска: ").strip().lower()

    found_products = [p for p in products if search_name in p['Название'].lower()]

    if found_products:
        print(f"\nНайдено товаров: {len(found_products)}")
        for product in found_products:
            print(f"  {product['Название']}: {product['Цена']} руб., {product['Количество']} шт.")
    else:
        print("Товары не найдены!")


def calculate_total_value(products):

    total_value = sum(p['Цена'] * p['Количество'] for p in products)
    print(f"\nОбщая стоимость всех товаров на складе: {total_value} руб.")
    return total_value


def display_products(products):

    if not products:
        print("Список товаров пуст!")
        return

    print("\n--- Список товаров ---")
    print(f"{'Название':<15} {'Цена':<10} {'Количество':<10}")
    print("-" * 35)
    for product in products:
        print(f"{product['Название']:<15} {product['Цена']:<10} {product['Количество']:<10}")


def main():

    if not os.path.exists('products.csv'):
        create_initial_csv()

    products = read_products()

    while True:
        print("\n" + "=" * 40)
        print("Управление складом продуктов")
        print("=" * 40)
        print("1. Просмотр всех товаров")
        print("2. Добавить новый товар")
        print("3. Поиск товара по названию")
        print("4. Расчет общей стоимости товаров")
        print("5. Сохранить и выйти")

        choice = input("\nВыберите действие (1-5): ").strip()

        if choice == '1':
            display_products(products)
        elif choice == '2':
            add_product(products)
        elif choice == '3':
            search_product(products)
        elif choice == '4':
            calculate_total_value(products)
        elif choice == '5':
            save_products(products)
            print("До свидания!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()