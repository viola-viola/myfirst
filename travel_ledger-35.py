# === Stage 35: Добавь рекомендации следующего действия на основе текущего состояния ===
# Project: TravelLedger
def suggest_next_action(current_state):
    """Recommend next action based on current travel planning state."""
    if not current_state.get('itinerary'):
        return "Create your first itinerary with destinations and dates"
    if not current_state.get('budget'):
        return "Set a travel budget to track expenses"
    if not current_state.get('documents'):
        return "Upload necessary travel documents (passport, visa, insurance)"
    if not current_state.get('bookings'):
        return "Book flights, hotels, and other services for your trip"
    if not current_state.get('notifications'):
        return "Set up notifications for flight updates and check-ins"
    if not current_state.get('reviews'):
        return "Leave reviews for places you visited to help other travelers"
    return "Your travel plan looks complete! Enjoy your trip!"
