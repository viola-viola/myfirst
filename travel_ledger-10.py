# === Stage 10: Добавь экспорт текущего состояния в JSON-строку ===
# Project: TravelLedger
def export_to_json():
    import json
    from datetime import datetime
    data = {
        "project": "TravelLedger",
        "timestamp": datetime.utcnow().isoformat(),
        "routes": routes,
        "bookings": bookings,
        "budget": budget,
        "documents": documents
    }
    return json.dumps(data, ensure_ascii=False, indent=2)
