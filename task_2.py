students = ["Иванов Иван:5,4,3,5", "Петров Петр:4,3,4,4", "Сидорова Мария:5,5,5,5"]
with open('students.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(students))

results = []
with open('students.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, scores = line.strip().split(':')
        avg = sum(map(int, scores.split(','))) / 4
        results.append((name, avg))

best = max(results, key=lambda x: x[1])
with open('result.txt', 'w', encoding='utf-8') as f:
    for name, avg in results:
        if avg > 4.0:
            f.write(f"{name}: {avg:.2f}\n")

print(f"Лучший: {best[0]} ({best[1]:.2f})")