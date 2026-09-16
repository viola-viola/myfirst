# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: TravelLedger
import sys

def _color_off():
    for code in _COLORS:
        print(code, end='', file=sys.stderr)
    print('', end='', file=sys.stderr)

def _color_on():
    for code in _COLORS:
        print(code, end='', file=sys.stderr)
    print('', end='', file=sys.stderr)

_COLORS = [
    '\033[0m', '\033[1m', '\033[4m', '\033[22m', '\033[24m',
    '\033[31m', '\033[32m', '\033[33m', '\033[34m', '\033[35m',
    '\033[36m', '\033[37m',
]

def colorize(text: str, fg: int = 0, bg: int = 0) -> str:
    if not os.environ.get('NO_COLOR', ''):
        return f'\033[{fg};{bg}m{text}\033[0m'
    return text

def info(text: str) -> str:
    return colorize(f'[INFO]  {text}', 36)

def success(text: str) -> str:
    return colorize(f'[OK]    {text}', 32)

def warning(text: str) -> str:
    return colorize(f'[WARN]  {text}', 33)

def error_text(text: str) -> str:
    return colorize(f'[ERR]   {text}', 31)

def debug(text: str) -> str:
    return colorize(f'[DBG]   {text}', 37)
