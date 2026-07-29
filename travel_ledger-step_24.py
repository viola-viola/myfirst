# === Stage 24: Добавь компактный вывод одной записи с деталями ===
# Project: TravelLedger
def print_record(rec):
    if rec is None:
        return "Нет данных"
    lines = [f"{rec.get('type', '?')} — {rec.get('id', '?')}", f"  {rec.get('title', '')}"]
    for k, v in rec.items():
        if isinstance(v, list) and not isinstance(v[0], dict):
            continue
        lines.append(f"  {k}: {v}")
    return "\n".join(lines)
