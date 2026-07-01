# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: TravelLedger
def main():
    print("=== TravelLedger CLI ===")
    while True:
        cmd = input("\nКоманда (1-4, q=выход): ").strip()
        if cmd == "q": break
        elif cmd in ("1", "2", "3"): print(f"Блок {cmd}: функционал в разработке.")
        else: print("Неизвестная команда.")

if __name__ == "__main__": main()
