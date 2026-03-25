import json
import os


class LibrarySystem:
    def __init__(self, filename="library.json"):
        self.filename = filename
        self.books = []
        self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            try:
                with open(self.filename, 'r', encoding='utf-8') as f:
                    self.books = json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                self.books = []
        else:
            self.books = []

    def save_data(self):
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(self.books, f, ensure_ascii=False, indent=4)

    def get_next_id(self):
        return max([b['id'] for b in self.books], default=0) + 1

    def view_all_books(self):
        if not self.books:
            print("\nБиблиотека пуста\n")
            return

        print("\n" + "=" * 60)
        for book in self.books:
            status = "Доступна" if book['available'] else "Взята"
            print(f"ID: {book['id']} | {book['title']} | {book['author']} | {status}")
        print("=" * 60 + f"\nВсего: {len(self.books)} книг\n")

    def search_books(self, query):
        results = [b for b in self.books if query.lower() in b['title'].lower()
                   or query.lower() in b['author'].lower()]

        if results:
            print(f"\nНайдено {len(results)} книг:")
            for book in results:
                status = "доступна" if book['available'] else "взята"
                print(f"  {status} {book['title']} - {book['author']}")
        else:
            print(f"\nПо запросу '{query}' ничего не найдено")
        print()

    def add_book(self, title, author, year, genre):
        new_book = {
            'id': self.get_next_id(),
            'title': title,
            'author': author,
            'year': year,
            'genre': genre,
            'available': True
        }
        self.books.append(new_book)
        self.save_data()
        print(f"Книга '{title}' добавлена (ID: {new_book['id']})\n")

    def change_status(self, book_id):
        for book in self.books:
            if book['id'] == book_id:
                book['available'] = not book['available']
                status = "доступна" if book['available'] else "взята"
                self.save_data()
                print(f"Статус книги '{book['title']}' изменен на '{status}'\n")
                return
        print(f"Книга с ID {book_id} не найдена\n")

    def delete_book(self, book_id):
        for i, book in enumerate(self.books):
            if book['id'] == book_id:
                title = book['title']
                del self.books[i]
                self.save_data()
                print(f"Книга '{title}' удалена\n")
                return
        print(f"Книга с ID {book_id} не найдена\n")

    def export_available(self, filename="available_books.txt"):
        available = [b for b in self.books if b['available']]

        if not available:
            print("Нет доступных книг\n")
            return

        with open(filename, 'w', encoding='utf-8') as f:
            f.write("ДОСТУПНЫЕ КНИГИ\n")
            f.write("=" * 50 + "\n")
            for book in available:
                f.write(f"{book['title']} - {book['author']} ({book['year']})\n")

        print(f"Экспортировано {len(available)} книг в {filename}\n")


def main():
    lib = LibrarySystem()

    while True:
        print("\n" + "=" * 40)
        print("БИБЛИОТЕКА")
        print("=" * 40)
        print("1. Все книги")
        print("2. Поиск")
        print("3. Добавить книгу")
        print("4. Изменить статус")
        print("5. Удалить книгу")
        print("6. Экспорт доступных")
        print("7. Выход")
        print("=" * 40)

        choice = input("Выберите действие (1-7): ")

        if choice == '1':
            lib.view_all_books()

        elif choice == '2':
            query = input("Введите название или автора: ")
            lib.search_books(query)

        elif choice == '3':
            print("\n--- Новая книга ---")
            title = input("Название: ")
            author = input("Автор: ")
            year_input = input("Год: ")
            genre = input("Жанр: ")

            if not title or not author or not year_input or not genre:
                print("Заполните все поля\n")
                continue

            if not year_input.isdigit():
                print("Год должен быть числом\n")
                continue

            lib.add_book(title, author, int(year_input), genre)

        elif choice == '4':
            book_id_input = input("ID книги: ")

            if not book_id_input.isdigit():
                print("ID должен быть числом\n")
                continue

            lib.change_status(int(book_id_input))

        elif choice == '5':
            book_id_input = input("ID книги: ")

            # Проверка что ID - число
            if not book_id_input.isdigit():
                print("ID должен быть числом\n")
                continue

            lib.delete_book(int(book_id_input))

        elif choice == '6':
            lib.export_available()

        elif choice == '7':
            print("\nДо свидания!\n")
            break

        else:
            print("Неверный выбор\n")


if __name__ == "__main__":
    main()