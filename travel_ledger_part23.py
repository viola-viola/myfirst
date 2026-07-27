# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: TravelLedger
def print_table(headers, rows):
    """Простой вывод данных в виде отформатированной таблицы."""
    col_widths = [len(str(h)) for h in headers]
    for row in rows:
        for i, val in enumerate(row):
            if i < len(col_widths) and len(str(val)) > col_widths[i]:
                col_widths[i] = len(str(val))

    separator = '+'.join('-' * (w + 2) for w in col_widths)
    header_line = '| ' + ' | '.join(str(h).ljust(col_widths[i]) for i, h in enumerate(headers)) + ' |'
    print(separator)
    print(header_line)
    print(separator)
    for row in rows:
        line = '| ' + ' | '.join(str(val).ljust(col_widths[i]) if i < len(row) else '' for i, val in enumerate(row)) + ' |'
        print(line)
    print(separator)

# Пример использования (удалить после проверки):
# print_table(["Название", "Цена", "Статус"], [
#     ["Отель Alpha", 150.5, "Подтверждено"],
#     ["Авиабилет Beta", 200.0, "Ожидание"]
# ])
