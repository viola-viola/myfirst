# === Stage 27: Добавь функции сброса демо-данных и очистки состояния ===
# Project: TravelLedger
def clear_state():
    """Сброс демо-данных: очистка маршрутов, бронирований, бюджета и документов."""
    global routes, bookings, budget, documents, currency, exchange_rate
    routes = []
    bookings = []
    budget = {}
    documents = []
    currency = "USD"
    exchange_rate = 1.0
