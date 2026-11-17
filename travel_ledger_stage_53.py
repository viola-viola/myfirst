# === Stage 53: Добавь импорт отчёта или списка записей из простого текстового формата ===
# Project: TravelLedger
def import_from_file(path):
    """Импорт отчёта или списка записей из простого текстового формата.

    Поддерживает два формата:
    1) Строки вида 'Ключ: Значение' (отчёт).
    2) Строки, начинающиеся с '#', как комментарии (список записей).
    """
    records = []
    report = {}
    with open(path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if ':' in line:
                key, value = line.split(':', 1)
                report[key.strip()] = value.strip()
            else:
                records.append(line)
    return report, records
