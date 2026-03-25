lines = ["Первая строка", "Вторая строка текста", "Третья", "Четвертая строка", "Пятая"]
with open('text.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

with open('text.txt', 'r', encoding='utf-8') as f:
    data = [line.strip() for line in f]

print(f"Строк: {len(data)}")
print(f"Слов: {sum(len(line.split()) for line in data)}")
print(f"Самая длинная строка: {max(data, key=len)}")