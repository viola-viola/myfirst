# === Stage 51: Добавь журнал изменений данных с отметками времени ===
# Project: TravelLedger
import time

class ChangeLog:
    def __init__(self):
        self._log = []

    def record(self, entity, action, record_id, old_value=None, new_value=None):
        self._log.append({
            "entity": entity,
            "action": action,
            "record_id": record_id,
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "old_value": old_value,
            "new_value": new_value,
        })

    def get_changes(self):
        return self._log

    def get_changes(self, entity=None, limit=20):
        if entity is not None:
            self._log = [c for c in self._log if c["entity"] == entity]
        return self._log[-limit:]

    def clear(self):
        self._log.clear()

CHANGE_LOG = ChangeLog()
