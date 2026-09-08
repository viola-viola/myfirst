# === Stage 37: Добавь мини-набор unit-тестов без внешних зависимостей ===
# Project: TravelLedger
import unittest

class TestTravelLedger(unittest.TestCase):
    def test_add_trip(self):
        ledger = TravelLedger()
        trip = Trip("Paris", "2024-06-01", "2024-06-07")
        ledger.add_trip(trip)
        self.assertEqual(len(ledger.trips), 1)

    def test_add_booking(self):
        ledger = TravelLedger()
        booking = Booking("Hotel A", 200.0, "2024-06-01", "2024-06-05", "confirmed")
        ledger.add_booking(booking)
        self.assertEqual(len(ledger.bookings), 1)

    def test_add_document(self):
        ledger = TravelLedger()
        doc = Document("passport.pdf", "12345678", "2024-01-01", "2030-01-01")
        ledger.add_document(doc)
        self.assertEqual(len(ledger.documents), 1)

    def test_add_route(self):
        ledger = TravelLedger()
        route = Route("Paris", "Lyon", 300.0, "2024-06-03", "train")
        ledger.add_route(route)
        self.assertEqual(len(ledger.routes), 1)

    def test_total_cost(self):
        ledger = TravelLedger()
        booking = Booking("Hotel A", 200.0, "2024-06-01", "2024-06-05", "confirmed")
        route = Route("Paris", "Lyon", 300.0, "2024-06-03", "train")
        ledger.add_booking(booking)
        ledger.add_route(route)
        self.assertEqual(ledger.total_cost, 500.0)

    def test_total_cost_empty(self):
        ledger = TravelLedger()
        self.assertEqual(ledger.total_cost, 0.0)

    def test_total_cost_with_documents(self):
        ledger = TravelLedger()
        booking = Booking("Hotel A", 200.0, "2024-06-01", "2024-06-05", "confirmed")
        route = Route("Paris", "Lyon", 300.0, "2024-06-03", "train")
        doc = Document("passport.pdf", "12345678", "2024-01-01", "2030-01-01")
        ledger.add_booking(booking)
        ledger.add_route(route)
        ledger.add_document(doc)
        self.assertEqual(ledger.total_cost, 500.0)

if __name__ == '__main__':
    unittest.main()
