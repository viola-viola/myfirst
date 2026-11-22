# === Stage 55: Добавь мягкую проверку дубликатов при создании записей ===
# Project: TravelLedger
def is_duplicate_record(records, new_data):
    normalized = {str(v).strip().lower(): v for v in new_data.values()}
    for r in records:
        if any(str(v).strip().lower() not in normalized for v in r.values()):
            continue
        match = all(str(r.get(k, "")).strip().lower() == str(v).strip().lower() for k, v in normalized.items())
        if match and r.get("id") != new_data.get("id"):
            return r
    return None

def check_for_duplicates(records, new_data):
    dup = is_duplicate_record(records, new_data)
    if dup:
        key = "id" if "id" in new_data else "route_id"
        return f"Запись дублирует существующую с id {dup.get(key)}"
    return None
