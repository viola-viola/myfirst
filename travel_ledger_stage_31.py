# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: TravelLedger
def switch_user_profile(username: str) -> None:
    """Переключить активный пользовательский профиль по имени."""
    global user_data
    if username not in user_data:
        raise ValueError(f"Профиль '{username}' не найден")
    active_username = [u for u, d in user_data.items() if d.get("active")][0]
    if active_username == username:
        print(f"Вы уже в роли {username}")
        return
    user_data[active_username]["active"] = False
    user_data[username]["active"] = True
    print(f"Профиль переключен на {username}")
