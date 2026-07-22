# === Stage 20: Добавь восстановление записей из архива ===
# Project: TravelLedger
import json, os

def recover_from_archive(archive_path):
    """Восстановляет записи из JSON-архива в структуру проекта."""
    if not archive_path or not os.path.exists(archive_path):
        print("Архив не найден")
        return
    with open(archive_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    for record in data.get('records', []):
        record_type = record.get('type', '')
        if record_type == 'route':
            routes.add_route(record['name'], record.get('destinations', []), record.get('budget', 0))
        elif record_type == 'booking':
            bookings.make_booking(record['hotel_name'], record.get('check_in'), record.get('check_out'), record.get('guests', []))
        elif record_type == 'expense':
            expenses.add_expense(record['category'], record['amount'])
        elif record_type == 'document':
            documents.upload_document(record['filename'], record.get('description', ''), record.get('file_path', ''))
