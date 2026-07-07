# === Stage 11: Добавь сохранение данных в локальный JSON-файл ===
# Project: TravelLedger
def save_to_json(data, filepath="travel_ledger.json"):
    """Сохраняет данные в JSON-файл."""
    import json
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print(f"Данные сохранены в {filepath}")
    except Exception as e:
        print(f"Ошибка сохранения: {e}")

def load_from_json(filepath="travel_ledger.json"):
    """Загружает данные из JSON-файла."""
    import json
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print("Файл не найден. Данные пока не сохранялись.")
        return {}
