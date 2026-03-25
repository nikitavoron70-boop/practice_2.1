import datetime


def read_last_operations(log_file, n=5):

    try:
        with open(log_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            last_lines = lines[-n:] if lines else []
            return last_lines
    except FileNotFoundError:
        return []


def write_operation(log_file, operation_str):

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {operation_str}\n"

    with open(log_file, 'a', encoding='utf-8') as file:
        file.write(log_entry)

    return log_entry


def clear_log(log_file):

    with open(log_file, 'w', encoding='utf-8') as file:
        file.write("")
    print("Лог-файл успешно очищен!")


def calculate():

    log_file = 'calculator.log'

    print("=" * 50)
    print("Последние 5 операций:")
    print("-" * 50)
    last_ops = read_last_operations(log_file, 5)

    if last_ops:
        for op in last_ops:
            print(op.strip())
    else:
        print("История операций пуста")

    print("=" * 50)

    while True:
        print("\n--- Калькулятор ---")
        print("1. Выполнить вычисление")
        print("2. Очистить лог")
        print("3. Выйти")

        choice = input("\nВыберите действие (1-3): ").strip()

        if choice == '1':
            try:
                num1 = float(input("Введите первое число: "))
                num2 = float(input("Введите второе число: "))
                operation = input("Введите операцию (+, -, *, /): ").strip()

                if operation == '+':
                    result = num1 + num2
                elif operation == '-':
                    result = num1 - num2
                elif operation == '*':
                    result = num1 * num2
                elif operation == '/':
                    if num2 == 0:
                        print("Ошибка: деление на ноль!")
                        continue
                    result = num1 / num2
                else:
                    print("Ошибка: неверная операция!")
                    continue

                operation_str = f"{num1} {operation} {num2} = {result}"

                print(f"Результат: {operation_str}")

                write_operation(log_file, operation_str)
                print("Операция записана в лог")

            except ValueError:
                print("Ошибка: введите корректные числа!")

        elif choice == '2':
            confirm = input("Вы уверены, что хотите очистить лог? (да/нет): ").strip().lower()
            if confirm == 'да':
                clear_log(log_file)

        elif choice == '3':
            print("До свидания!")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    calculate()