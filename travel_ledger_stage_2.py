# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: TravelLedger
class ValidationError(Exception): pass

def validate_date(date_str: str) -> tuple[str, bool]:
    try:
        year, month, day = map(int, date_str.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31): return date_str, False
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0): days_in_month[2] = 29
        if day > days_in_month[month]: return date_str, False
    except ValueError: return date_str, False
    return date_str, True

def validate_budget(amount: float) -> tuple[float, bool]:
    try:
        amount = round(float(amount), 2)
        if amount < 0: return amount, False
    except (ValueError, TypeError): return 0.0, False
    return amount, True

def validate_email(email: str) -> tuple[str, bool]:
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if not email or '@' not in email: return email, False
    if not re.match(pattern, email): return email, False
    return email, True

# === Stage 2: Добавь модели данных и функции валидации пользовательского ввода ===
# Project: TravelLedger
class ValidationError(Exception): pass

def validate_date(date_str: str) -> bool:
    try:
        year, month, day = map(int, date_str.split('-'))
        if not (1 <= month <= 12 and 1 <= day <= 31): return False
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if month == 2 and (year % 4 == 0 and year % 100 != 0 or year % 400 == 0): days_in_month[2] = 29
        return day <= days_in_month[month]
    except: return False

def validate_budget(budget_str: str) -> bool:
    try:
        val = float(budget_str.replace(',', '.'))
        return 0.0 < val <= 1e8
    except: return False

def validate_email(email: str) -> bool:
    import re; pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
