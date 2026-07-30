# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: TravelLedger
def sanitize_travel_date(date_str):
    """Парсит дату 'YYYY-MM-DD', возвращает str или raises ValueError."""
    if not date_str or len(date_str) != 10:
        raise ValueError(f"Некорректный формат даты: '{date_str}'")
    try:
        year, month, day = map(int, date_str.split('-'))
    except ValueError:
        raise ValueError(f"Некорректные числа в дате: '{date_str}'")
    
    if not (1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
        raise ValueError("Дни и месяцы вне допустимых диапазонов")

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        days_in_month[2] = 29

    if day > days_in_month[month]:
        raise ValueError(f"Дата {date_str} не существует")

    return date_str
