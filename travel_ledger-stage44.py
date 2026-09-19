# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: TravelLedger
def backup_data_file(source_path, backup_dir=None, backup_extension='.bak'):
    """Create a timestamped backup of the data file, optionally in a custom directory."""
    if backup_dir is None:
        backup_dir = '.'
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    filename = os.path.basename(source_path)
    backup_path = os.path.join(backup_dir, f'{filename}{backup_extension}({timestamp})')
    try:
        shutil.copy2(source_path, backup_path)
        return backup_path
    except FileNotFoundError:
        print(f'Error: source file not found: {source_path}')
        return None
