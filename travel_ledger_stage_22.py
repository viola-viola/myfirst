# === Stage 22: Добавь проверку просроченных напоминаний ===
# Project: TravelLedger
def check_overdue_reminders():
    """Проверяет напоминания, которые уже просрочены."""
    now = datetime.datetime.now(datetime.timezone.utc)
    overdue = []
    for reminder in reminders:
        if reminder['date'] < now and not reminder['done']:
            overdue.append(reminder)
    return overdue

overdue = check_overdue_reminders()
if overdue:
    print(f"⚠️  Просрочено {len(overdue)} напоминаний:")
    for r in overdue:
        days_left = (r['date'] - now).days
        print(f"   • {r.get('title', 'Без названия')} — было {days_left} дней назад")
