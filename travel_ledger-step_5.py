# === Stage 5: Добавь удаление записей и аккуратную обработку отсутствующих идентификаторов ===
# Project: TravelLedger
def delete_record(collection_name, record_id):
    if collection_name not in db:
        raise ValueError(f"Коллекция '{collection_name}' не существует")
    records = db[collection_name]
    if record_id not in records:
        return False  # Запись отсутствовала
    del records[record_id]
    return True

def handle_missing_identifier(collection_name, record_id):
    if collection_name not in db:
        print(f"Ошибка: коллекция '{collection_name}' не найдена.")
        return None
    if record_id is None or (isinstance(record_id, str) and len(record_id.strip()) == 0):
        print("Предупреждение: идентификатор записи пустой или отсутствует.")
        return None
    records = db[collection_name]
    if record_id not in records:
        print(f"Предупреждение: запись с ID '{record_id}' не найдена в коллекции '{collection_name}'.")
        return None
    del records[record_id]
    print(f"Запись с ID '{record_id}' успешно удалена из коллекции '{collection_name}'.")
    return True
