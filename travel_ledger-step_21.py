# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: TravelLedger
def add_reminder(reminder_text, due_date):
    """Добавляет напоминание с текстом и датой выполнения."""
    reminders = []
    if not hasattr(add_reminder, '_reminders'):
        add_reminder._reminders = reminders
    reminders.append({'text': reminder_text, 'due_date': due_date})
    return len(reminders)

def get_due_reminders(due_date):
    """Возвращает напоминания, срок которых наступил."""
    if not hasattr(add_reminder, '_reminders'):
        return []
    return [r for r in add_reminder._reminders if r['due_date'] <= due_date]

def clear_reminder(index):
    """Удаляет напоминание по индексу."""
    if not hasattr(add_reminder, '_reminders') or index >= len(add_reminder._reminders):
        return False
    removed = add_reminder._reminders.pop(index)
    return True

def get_all_reminders():
    """Возвращает все напоминания."""
    if not hasattr(add_reminder, '_reminders'):
        return []
    return list(add_reminder._reminders)
