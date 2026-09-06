# === Stage 36: Добавь проверку целостности данных и функцию ремонта простых проблем ===
# Project: TravelLedger
def verify_and_repair(data):
    """Проверка целостности и простой ремонт данных."""
    errors = []
    if not isinstance(data, dict):
        return data, ["Данные не валидны"]
    if "route" not in data:
        errors.append("route: отсутствует")
    if "route" in data and not isinstance(data["route"], dict):
        errors.append("route: не dict")
    if "route" in data and "legs" in data["route"] and not isinstance(data["route"]["legs"], list):
        errors.append("legs: не список")
    if "route" in data and "legs" in data["route"] and isinstance(data["route"]["legs"], list):
        for i, leg in enumerate(data["route"]["legs"]):
            if not isinstance(leg, dict):
                data["route"]["legs"][i] = {"distance": 0, "duration": 0, "stops": []}
    if "reservations" in data and not isinstance(data["reservations"], list):
        errors.append("reservations: не список")
    if "reservations" in data and isinstance(data["reservations"], list):
        for i, res in enumerate(data["reservations"]):
            if not isinstance(res, dict):
                data["reservations"][i] = {"type": "flight", "price": 0, "date": "", "status": "confirmed"}
    if "budget" in data and not isinstance(data["budget"], dict):
        errors.append("budget: не dict")
    if "budget" in data and "total" in data["budget"] and not isinstance(data["budget"]["total"], (int, float)):
        data["budget"]["total"] = 0.0
    if "documents" in data and not isinstance(data["documents"], list):
        errors.append("documents: не список")
    if "documents" in data and isinstance(data["documents"], list):
        for i, doc in enumerate(data["documents"]):
            if not isinstance(doc, dict):
                data["documents"][i] = {"name": "", "date": "", "status": "pending"}
    return data, errors if errors else ["Все данные на месте"]
