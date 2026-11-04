# === Stage 49: Добавь финальную самопроверку приложения и отчёт о готовности ===
# Project: TravelLedger
print("=" * 50)
print("TRAVELEDGER — ИТОГИ САМОПРОВЕРКИ")
print("=" * 50)

trips = _get("trips", [])
bookings = _get("bookings", [])
budgets = _get("budgets", [])
docs = _get("docs", [])

if not trips:
    print("⚠ Приложение пустое. Добавьте первую поездку.")
    print("=" * 50)
    print("ГОТОВНОСТЬ: 0%")
    print("=" * 50)
    exit()

ok, issues = [], []

for t in trips:
    routes = t.get("routes", [])
    if not routes:
        issues.append(f"✗ {t['name']}: нет маршрутов")
        continue
    if t.get("start_city") and t.get("end_city"):
        ok.append(f"✓ {t['name']}: маршрут {t['start_city']} → {t['end_city']}")
    tot = sum(b.get("cost", 0) for b in bookings if b.get("trip_id") == t["id"])
    bd = budgets.get(t["id"], {})
    spent = sum(b.get("amount", 0) for b in bookings if b.get("trip_id") == t["id"])
    limit = bd.get("limit", float("inf"))
    if spent > limit:
        issues.append(f"⚠ {t['name']}: перерасход {spent} / {limit}")
    elif spent > 0:
        ok.append(f"✓ {t['name']}: потрачено {spent} из {limit}")

if docs:
    ok.append(f"✓ Загружено {len(docs)} документов")

print("\n✅ Проверено:")
for x in ok:
    print("   ", x)

print("\n⚠️  Проблемы:")
for x in issues or ["—"]:
    print("   ", x)

score = int(len(ok) * 100 / max(1, len(ok) + len(issues)))
print("\n" + "=" * 50)
print(f"ГОТОВНОСТЬ: {score}%")
print("=" * 50)
