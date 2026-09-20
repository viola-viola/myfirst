# === Stage 45: Добавь восстановление из резервной копии ===
# Project: TravelLedger
import json

def restore_backup(backup_file, config):
    if not backup_file or not config:
        return False
    try:
        with open(backup_file, 'r', encoding='utf-8') as f:
            backup_data = json.load(f)
        config['itinerary'] = backup_data.get('itinerary', [])
        config['budget'] = backup_data.get('budget', {})
        config['documents'] = backup_data.get('documents', [])
        config['last_updated'] = backup_data.get('last_updated', '')
        return True
    except Exception:
        return False
