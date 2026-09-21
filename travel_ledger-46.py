# === Stage 46: Добавь миграцию версии структуры данных ===
# Project: TravelLedger
def migrate_v46():
    """Migration v46: add version field to all data structures."""
    if not hasattr(TravelLedger, '_version'):
        TravelLedger._version = 46
        print(f"[Migration v46] Structure version set to {TravelLedger._version}")
        return True
    print(f"[Migration v46] Already migrated to v{TravelLedger._version}")
    return True
