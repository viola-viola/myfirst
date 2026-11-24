# === Stage 56: Добавь массовое обновление выбранных записей ===
# Project: TravelLedger
def bulk_update_records(records, fields_map, updates, action):
    """Массовое обновление выбранных записей по списку полей.

    records - список словарей с выбранными записями.
    fields_map - словарь {id: список id записей}.
    updates - словарь {field: new_value}.
    action - функция обновления типа ('route', 'booking', 'budget', 'document').
    """
    updated = []
    for rec in records:
        rec_id = rec.get('id')
        if rec_id not in fields_map:
            continue
        ids = fields_map[rec_id]
        for rid in ids:
            try:
                action(rid, updates)
                updated.append(rid)
            except Exception as e:
                print(f"Ошибка обновления {rid}: {e}")
    print(f"Обновлено записей: {len(updated)}")
    return updated
