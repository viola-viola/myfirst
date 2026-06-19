# === Stage 1: Создай базовую структуру файла приложения, точку входа и демонстрационные данные ===
# Project: TravelLedger
from dataclasses import dataclass, field
from datetime import date
from typing import List, Optional
import uuid

@dataclass
class Trip:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    name: str = ""
    start_date: date = None
    end_date: date = None
    budget: float = 0.0
    status: str = "draft"

@dataclass
class Booking:
    id: str = field(default_factory=lambda: str(uuid.uuid4()))
    trip_id: str = ""
    type: str = ""
    cost: float = 0.0
    date: date = None

def get_demo_data() -> dict:
    return {
        "trips": [Trip(name="Европа", start_date=date(2024, 6, 1), end_date=date(2024, 6, 30), budget=5000.0)],
        "bookings": [Booking(trip_id="", type="flight", cost=800.0, date=date(2024, 6, 1))]
    }

if __name__ == "__main__":
    demo = get_demo_data()
    print(f"Демо-данные: {len(demo['trips'])} поездок и {len(demo['bookings'])} бронирований.")
