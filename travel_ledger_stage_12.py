# === Stage 12: Добавь загрузку данных из локального JSON-файла с обработкой ошибок ===
# Project: TravelLedger
def load_json_file(path, default=None):
    if default is None:
        default = {}
    try:
        with open(path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data if isinstance(data, dict) else default
    except FileNotFoundError:
        print(f"[TravelLedger] Файл не найден: {path}")
        return default
    except json.JSONDecodeError as e:
        print(f"[TravelLedger] Ошибка JSON в файле {path}: {e}")
        return default
    except Exception as e:
        print(f"[TravelLedger] Неожиданная ошибка при загрузке {path}: {type(e).__name__}: {e}")
        return default
