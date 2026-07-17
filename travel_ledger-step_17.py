# === Stage 17: Добавь группировку записей по категориям ===
# Project: TravelLedger
def categorize_entries(entries):
    categories = {
        'transport': 0,
        'accommodation': 0,
        'food': 0,
        'activities': 0,
        'other': 0,
    }
    for entry in entries:
        if not entry.get('category'):
            entry['category'] = 'other'
        categories[entry['category']] += entry['amount']
    return categories
