# === Stage 3: Реализуй хранение состояния в памяти и функции добавления записей ===
# Project: TravelLedger
class TravelLedger:
    def __init__(self):
        self._routes = {}
        self._bookings = []
        self._budgets = {}
        self._documents = []
    
    def add_route(self, name, city_from, city_to, distance_km=0):
        self._routes[name] = {"city_from": city_from, "city_to": city_to, "distance_km": distance_km}
    
    def add_booking(self, route_name, date_str, price_usd, status="confirmed"):
        booking_id = len(self._bookings) + 1
        self._bookings.append({
            "id": booking_id,
            "route_name": route_name,
            "date": date_str,
            "price_usd": float(price_usd),
            "status": status
        })
    
    def add_budget(self, category, amount_usd):
        self._budgets[category] = {"amount_usd": float(amount_usd), "spent_usd": 0.0}
    
    def add_document(self, name, file_path_or_url, description=""):
        doc_id = len(self._documents) + 1
        self._documents.append({
            "id": doc_id,
            "name": name,
            "file_path_or_url": file_path_or_url,
            "description": description
        })
