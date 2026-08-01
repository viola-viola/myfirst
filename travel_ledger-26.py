# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: TravelLedger
def demo_run():
    print("=== TravelLedger Demo ===")
    trip = Trip(name="Paris 2025", budget=1500)
    for i in range(3):
        route = Route(trip, day=i+1, city=["Paris","Lyon","Marseille"][i], dist=120 + i*80)
        trip.add_route(route)
    booking_hotel = Booking(trip, "Hotel", 600)
    booking_flight = Booking(trip, "Flight", 350)
    trip.book(booking_hotel, booking_flight)
    doc = Document(trip, "itinerary.pdf")
    trip.add_document(doc)
    print(f"Trip: {trip.name}")
    for r in trip.routes: print(f"Day {r.day}: {r.city} ({r.dist}km)")
    print(f"Bookings: hotel={booking_hotel.cost}, flight={booking_flight.cost}")
    doc.show()
