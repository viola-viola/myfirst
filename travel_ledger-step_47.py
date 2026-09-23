# === Stage 47: Добавь финальную функцию demo(), которая показывает основной пользовательский сценарий ===
# Project: TravelLedger
def demo():
    """Демонстрация основного сценария: создание маршрута, бронирование, расчёт бюджета."""
    from travel_ledger import TravelLedger

    app = TravelLedger()

    # 1. Создаём маршрут
    route = app.create_route(
        name="Поездка в Грузию",
        origin="Москва",
        destination="Тбилиси",
        transport="самолёт",
        distance_km=2500,
        budget_total=5000,
        budget_currency="RUB",
    )
    print(f"Маршрут создан: {route.name} ({route.transport}, {route.distance_km} км)")

    # 2. Добавляем бронирования
    flight = app.book_flight(
        route_id=route.id,
        departure="2026-07-15",
        return_date="2026-07-22",
        passenger_count=2,
        airline="Aeroflot",
        price_per_person=35000,
        seat_class="эконом",
    )
    print(f"Бронь: {flight.airline}, {flight.departure} -> {flight.return_date}, цена: {flight.total_price} RUB")

    hotel = app.book_hotel(
        route_id=route.id,
        check_in="2026-07-15",
        check_out="2026-07-22",
        room_type="стандарт",
        price_per_night=2500,
        nights=7,
        guests=2,
    )
    print(f"Отель: {hotel.room_type}, {hotel.total_price} RUB за {hotel.nights} ночей")

    # 3. Расчёт бюджета
    budget = app.calculate_budget(route_id=route.id)
    print(f"\nБюджет поездки:")
    print(f"  Общая стоимость: {budget.total_cost} {budget.currency}")
    print(f"  Остаток: {budget.remaining} {budget.currency}")
    print(f"  Статус: {'В рамках бюджета' if budget.status == 'in_budget' else 'ПЕРЕБЮДЖЕТ' if budget.status == 'over' else 'Неизвестно'}")

    # 4. Добавляем документ
    doc = app.add_document(
        route_id=route.id,
        title="Паспорт",
        file_name="passport.jpg",
        file_size=500,
        file_type="image",
        upload_date="2026-07-01",
    )
    print(f"\nДокумент добавлен: {doc.title} ({doc.file_size} байт)")

    # 5. Сохраняем и выводим итог
    app.save_route(route_id=route.id)
    print(f"\nИтоговая стоимость маршрута: {app.get_route_total_cost(route_id=route.id)}")

    print("\n=== Демо завершено ===")

if __name__ == "__main__":
    demo()
