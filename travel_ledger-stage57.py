# === Stage 57: Добавь массовое удаление с подтверждением через параметр ===
# Project: TravelLedger
def bulk_delete_trips(trips, trip_ids, confirm=True):
    if not trip_ids:
        print("Удалить нечего.")
        return
    ids = set(trip_ids)
    if confirm:
        print("Удалить поездки:", ", ".join(ids))
        resp = input("Подтвердите (y/N): ").strip().lower()
        if resp != "y":
            print("Отмена.")
            return
    removed = [t for t in trips if t["id"] in ids]
    for t in removed:
        trips.remove(t)
        print("Удалена поездка:", t["id"])
    print("Осталось поездок:", len(trips))
