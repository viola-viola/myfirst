# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: TravelLedger
import json, sys, os

def load_initial_data(json_string: str) -> dict:
    try:
        data = json.loads(json_string)
        if not isinstance(data, dict):
            raise ValueError("JSON должен содержать объект")
        return {
            "routes": data.get("routes", []),
            "bookings": data.get("bookings", []),
            "budget": data.get("budget", {"total": 0, "spent": 0}),
            "documents": data.get("documents", [])
        }
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}")
        sys.exit(1)

if __name__ == "__main__":
    sample_json = '{"routes":[{"id":"r1","city":"Москва"},{"id":"r2","city":"Санкт-Петербург"}],"bookings":[],"budget":{"total":5000,"spent":1200},"documents":[{"type":"паспорт","status":"действителен"}]}'
    initial_state = load_initial_data(sample_json)
    print(f"Загружено {len(initial_state['routes'])} маршрутов и {len(initial_state['bookings'])} бронирований")
