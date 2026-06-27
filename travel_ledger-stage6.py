# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: TravelLedger
def filter_records(status=None, category=None, tags=None):
    filtered = []
    for record in records:
        if status and record.get('status') != status:
            continue
        if category and record.get('category') != category:
            continue
        if tags is not None:
            rec_tags = set(record.get('tags', []))
            if not any(tag in rec_tags for tag in tags):
                continue
        filtered.append(record)
    return filtered

def get_records_by_status(status):
    return filter_records(status=status)

def get_records_by_category(category):
    return filter_records(category=category)

def get_records_by_tags(*tags):
    if not tags:
        return records[:]
    tag_set = set(tags)
    return [r for r in records if any(t in r.get('tags', []) for t in tag_set)]
