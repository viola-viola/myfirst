# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: TravelLedger
def add_user_profile(username, email, budget_limit, currency="USD"):
    """Добавляет нового пользователя и сохраняет его профиль."""
    profiles = []
    with open("profiles.txt", "a") as f:
        f.write(f"{username}|{email}|{budget_limit}|{currency}\n")
    return profiles
