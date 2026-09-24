# === Stage 48: Проведи рефакторинг: разнеси крупные функции, сохрани совместимость публичных команд ===
# Project: TravelLedger
def parse_date_input(date_str):
    """Parse date string in multiple formats to a tuple (year, month, day)."""
    formats = [
        "%Y-%m-%d", "%d.%m.%Y", "%d/%m/%Y", "%m/%d/%Y",
        "%Y/%m/%d", "%d-%m-%Y", "%m-%d-%Y",
    ]
    for fmt in formats:
        try:
            return datetime.strptime(date_str, fmt)
        except ValueError:
            continue
    raise ValueError(f"Не удалось распарсить дату: {date_str}")
