# === Stage 19: Добавь функцию архивации завершённых или старых записей ===
# Project: TravelLedger
def archive_records(ledger, cutoff_days=365):
    """Archive records older than cutoff_days."""
    import datetime
    cutoff = datetime.datetime.now() - datetime.timedelta(days=cutoff_days)
    archived = []
    for rec in ledger.records:
        if isinstance(rec.get('created'), datetime.datetime) and rec['created'] < cutoff:
            rec['status'] = 'archived'
            archived.append(rec)
    return archived
