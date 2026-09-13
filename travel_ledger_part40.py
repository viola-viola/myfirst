# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: TravelLedger
import argparse

def main():
    parser = argparse.ArgumentParser(description="TravelLedger CLI")
    sub = parser.add_subparsers(dest="command")
    sub.add_parser("init")
    sub.add_parser("routes")
    sub.add_parser("book")
    sub.add_parser("budget")
    sub.add_parser("docs")
    sub.add_parser("summary")
    args = parser.parse_args()
    print(f"TravelLedger v40: command '{args.command}'")

main()
