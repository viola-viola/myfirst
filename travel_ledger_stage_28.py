# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: TravelLedger
def compute_project_metrics():
    """Выводит ключевые метрики проекта TravelLedger."""
    # Пример метрик (замените на реальные данные из вашего проекта):
    total_routes = 15
    total_bookings = 8
    total_budget = 15000.0
    total_documents = 3
    total_travelers = 5
    avg_trip_duration_days = 7.2

    metrics = {
        "total_routes": total_routes,
        "total_bookings": total_bookings,
        "total_budget": total_budget,
        "total_documents": total_documents,
        "total_travelers": total_travelers,
        "avg_trip_duration_days": avg_trip_duration_days,
    }

    print("=" * 40)
    print("TravelLedger — Ключевые метрики проекта")
    print("=" * 40)
    for key, value in metrics.items():
        print(f"{key}: {value}")
    print("=" * 40)

    # Выводим в формате JSON для удобства парсинга
    import json
    print(json.dumps(metrics, indent=2))

    return metrics
