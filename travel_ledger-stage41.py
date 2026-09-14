# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: TravelLedger
def dry_run(operation, payload):
    """Simulate an operation and print what would happen without actually doing it.

    Supported operations:
        'add_trip', 'add_route', 'add_booking', 'add_document',
        'remove_trip', 'remove_route', 'remove_booking', 'remove_document',
        'update_trip', 'update_route', 'update_booking', 'update_document'

    Returns the simulated result as a dict.
    """
    print(f"[DRY-RUN] {operation}({payload})")
    return {"status": "simulated", "operation": operation, "payload": payload}
