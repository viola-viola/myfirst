# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: TravelLedger
def sort_records(records, key='date'):
    if not records: return []
    order_map = {'date': 'departure_date', 'priority': 'priority', 'name': 'destination'}
    field = order_map.get(key.lower(), 'departure_date')
    reverse = False
    if key == 'priority':
        def _sort_pri(r): return -r['priority']
        return sorted(records, key=_sort_pri)
    try:
        return sorted(records, key=lambda r: (None if not r.get(field) else r[field], r.get('destination', '')))
    except TypeError:
        return records
