# === Stage 32: Добавь журнал действий пользователя ===
# Project: TravelLedger
class ActionLog:
    def __init__(self):
        self.entries = []
    
    def add(self, user, action, timestamp=None):
        timestamp = timestamp or datetime.now()
        self.entries.append({'user': user, 'action': action, 'timestamp': timestamp})
        return self.entries[-1]
    
    def get(self, user=None):
        if user:
            return [e for e in self.entries if e['user'] == user]
        return list(self.entries)
    
    def clear(self):
        self.entries.clear()
