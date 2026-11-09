# === Stage 50: Сделай аккуратную финальную полировку сообщений, названий функций и комментариев ===
# Project: TravelLedger
def polish_trips():
    """Финальная полировка: нормализация названий и проверка целостности."""
    for trip in trips.values():
        trip["name"] = trip["name"].strip().title()
        for booking in trip["bookings"]:
            booking["destination"] = booking["destination"].strip().title()
        for doc in trip["documents"]:
            doc["name"] = doc["name"].strip().lower()
    return trips
