# === Stage 52: Добавь экспорт краткого отчёта в текстовом формате ===
# Project: TravelLedger
def export_report(trips):
    lines = ["TravelLedger - Краткий отчёт", "=" * 40]
    for trip in trips:
        title = f"Маршрут: {trip.get('title', 'Без названия')}"
        lines.append(title)
        lines.append("-" * len(title))
        if trip.get("destinations"):
            dests = ", ".join(d for d in trip["destinations"][:5])
            lines.append(f"Места: {dests}")
        if trip.get("bookings"):
            n = len(trip["bookings"])
            lines.append(f"Бронирований: {n}")
        if trip.get("budget"):
            lines.append(f"Бюджет: {trip['budget']}")
        if trip.get("documents"):
            docs = ", ".join(trip["documents"][:5])
            lines.append(f"Документы: {docs}")
        lines.append("")
    return "\n".join(lines)
