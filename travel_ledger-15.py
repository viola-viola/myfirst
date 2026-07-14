# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: TravelLedger
import json, os, datetime

def weekly_stats(filepath):
    if not os.path.exists(filepath) or os.path.getsize(filepath) == 0:
        return []
    records = json.loads(open(filepath).read())
    stats = {}
    for r in records:
        date_s = str(r.get('date', '')).strip()
        if not date_s: continue
        try:
            d = datetime.datetime.strptime(date_s, '%Y-%m-%d')
        except ValueError:
            try:
                d = datetime.datetime.strptime(date_s[:10], '%Y%m%d')
            except Exception:
                continue
        week_key = d.strftime('%G-W%V')
        stats[week_key] = {'count': 0, 'total': 0.0}
    for r in records:
        date_s = str(r.get('date', '')).strip()
        if not date_s: continue
        try:
            d = datetime.datetime.strptime(date_s, '%Y-%m-%d')
        except ValueError:
            try:
                d = datetime.datetime.strptime(date_s[:10], '%Y%m%d')
            except Exception:
                continue
        week_key = d.strftime('%G-W%V')
        if week_key in stats:
            stats[week_key]['count'] += 1
            stats[week_key]['total'] += float(r.get('cost', r.get('amount', 0.0)) or 0)
    return sorted(stats.items())

def print_weekly_stats(filepath):
    w = weekly_stats(filepath)
    if not w:
        print("Нет данных для статистики.")
        return
    for week, info in w:
        print(f"Неделя {week}: {info['count']} операций, сумма {info['total']:.2f}")

if __name__ == '__main__':
    print_weekly_stats('travel_ledger_data.json')
