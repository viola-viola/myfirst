# === Stage 14: Добавь генерацию краткой сводки по текущим данным ===
# Project: TravelLedger
def generate_summary():
    """Генерирует краткую сводку по текущим данным проекта."""
    total_trips = len(trips)
    total_bookings = sum(len(b.bookings) for b in bookings if b.bookings)
    total_docs = sum(len(d.documents) for d in documents if d.documents)
    
    print(f"=== СВОДКА TravelLedger ===")
    print(f"Маршрутов: {total_trips}")
    print(f"Бронирований: {total_bookings}")
    print(f"Документов: {total_docs}")
    
    if total_trips > 0:
        avg_cost = sum(trip.total_cost for trip in trips) / total_trips
        print(f"Средняя стоимость маршрута: {avg_cost:.2f} EUR")
