# === Stage 54: Добавь режим избранных записей и быстрый доступ к ним ===
# Project: TravelLedger
def add_favorite(trip_id):
    for t in trips:
        if t["id"] == trip_id:
            t["favorites"].add(trip_id)
            save_trips()
            print(f"Добавлено в избранное: {t['name']}")
            return
    print("Поездка не найдена")

def remove_favorite(trip_id):
    for t in trips:
        if t["id"] == trip_id:
            t["favorites"].discard(trip_id)
            save_trips()
            print(f"Удалено из избранного: {t['name']}")
            return
    print("Поездка не найдена")

def list_favorites():
    favs = [t for t in trips if t["favorites"]]
    if not favs:
        print("Избранное пусто")
        return
    print("Избранные поездки:")
    for t in favs:
        print(f"  [{t['id']}] {t['name']} ({t['destination']})")

def quick_access_favorites():
    print("Быстрый доступ к избранным:")
    for t in trips:
        if t["favorites"]:
            print(f"  {t['id']} - {t['name']}")
            for b in t["bookings"]:
                print(f"    - Бронь {b['id']}: {b['type']} {b['date']}")
            for d in t["documents"]:
                print(f"    - Документ {d['id']}: {d['name']}")
