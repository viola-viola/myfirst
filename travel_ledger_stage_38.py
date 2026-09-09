# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: TravelLedger
import unittest
from travel_ledger import (
    TravelLedger, Route, Booking, Budget, Document, TravelPlan
)

class TestEdgeCases(unittest.TestCase):

    def test_empty_route(self):
        route = Route("Empty", [], [], [], [])
        self.assertEqual(route.get_route_summary(), "Empty route")
        self.assertEqual(route.get_total_distance(), 0)

    def test_zero_budget(self):
        budget = Budget(0, 0)
        self.assertEqual(budget.get_remaining(), 0)
        self.assertEqual(budget.get_percentage_spent(), 0)

    def test_booking_exact_budget(self):
        ledger = TravelLedger()
        booking = Booking("Exact", 100, "Hotel", 100)
        ledger.add_booking(booking)
        budget = Budget(100, 100)
        ledger.set_budget(budget)
        self.assertEqual(ledger.get_budget_remaining(), 0)
        self.assertEqual(ledger.get_budget_percentage_spent(), 100)

    def test_booking_exceeds_budget(self):
        ledger = TravelLedger()
        booking = Booking("Over", 100, "Flight", 150)
        ledger.add_booking(booking)
        budget = Budget(100, 150)
        ledger.set_budget(budget)
        self.assertEqual(ledger.get_budget_remaining(), -50)
        self.assertEqual(ledger.get_budget_percentage_spent(), 150)

    def test_document_empty(self):
        doc = Document("Empty", "", "")
        self.assertEqual(doc.get_document_type(), "Empty")

    def test_travel_plan_empty(self):
        plan = TravelPlan("Empty", "Empty", [])
        self.assertEqual(plan.get_travel_summary(), "Empty")

    def test_multiple_routes(self):
        route1 = Route("Route1", [10, 20], [2024, 2025], ["A"], [])
        route2 = Route("Route2", [30, 40], [2025, 2026], ["B"], [])
        route3 = Route("Route3", [50, 60], [2026, 2027], ["C"], [])
        self.assertEqual(len(route1.get_route_details()), 2)
        self.assertEqual(len(route2.get_route_details()), 2)
        self.assertEqual(len(route3.get_route_details()), 2)

    def test_multiple_bookings(self):
        ledger = TravelLedger()
        booking1 = Booking("Booking1", 100, "Hotel", 100)
        booking2 = Booking("Booking2", 200, "Flight", 200)
        booking3 = Booking("Booking3", 300, "Car", 300)
        ledger.add_booking(booking1)
        ledger.add_booking(booking2)
        ledger.add_booking(booking3)
        self.assertEqual(len(ledger.get_bookings()), 3)
        self.assertEqual(ledger.get_total_bookings_cost(), 600)

    def test_multiple_budgets(self):
        budget1 = Budget(100, 100)
        budget2 = Budget(200, 200)
        budget3 = Budget(300, 300)
        self.assertEqual(budget1.get_remaining(), 0)
        self.assertEqual(budget2.get_remaining(), 0)
        self.assertEqual(budget3.get_remaining(), 0)

    def test_multiple_documents(self):
        doc1 = Document("Doc1", "Document1", "Description1")
        doc2 = Document("Doc2", "Document2", "Description2")
        doc3 = Document("Doc3", "Document3", "Description3")
        self.assertEqual(doc1.get_document_type(), "Doc1")
        self.assertEqual(doc2.get_document_type(), "Doc2")
        self.assertEqual(doc3.get_document_type(), "Doc3")

    def test_multiple_travel_plans(self):
        plan1 = TravelPlan("Plan1", "Destination1", [])
        plan2 = TravelPlan("Plan2", "Destination2", [])
        plan3 = TravelPlan("Plan3", "Destination3", [])
        self.assertEqual(plan1.get_travel_summary(), "Plan1")
        self.assertEqual(plan2.get_travel_summary(), "Plan2")
        self.assertEqual(plan3.get_travel_summary(), "Plan3")

if __name__ == '__main__':
    unittest.main()
