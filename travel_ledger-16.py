# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: TravelLedger
def monthly_stats():
    today = datetime.date.today()
    month, year = today.month, today.year
    stats = {"days": 0, "travel_days": 0, "active_days": 0}
    if month == 1:
        for d in range(366):
            stat_date = date(year + d // 365, (d % 365) // 30 + 1, (d % 365) % 28 + 1)
            if stat_date >= today:
                is_travel_day = any(trip['start'] <= stat_date <= trip['end'] for trip in trips if isinstance(trip, dict))
                is_active = not all(b["status"] == "cancelled" for b in bookings if isinstance(b, dict))
                stats["days"] += 1
                if is_travel_day: stats["travel_days"] += 1
                if is_active: stats["active_days"] += 1
    return stats
