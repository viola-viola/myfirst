# === Stage 13: Добавь поиск по нескольким полям без учёта регистра ===
# Project: TravelLedger
def search_by_multiple_fields(records, fields):
    """Поиск записей по нескольким полям без учёта регистра."""
    result = []
    for record in records:
        match = True
        for field_name, value in fields.items():
            if field_name not in record or str(record[field_name]).lower() != value.lower():
                match = False
                break
        if match:
            result.append(record)
    return result
