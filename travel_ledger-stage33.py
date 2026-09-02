# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: TravelLedger
class UndoManager:
    def __init__(self):
        self._history = []

    def push(self, action):
        self._history.append(action)

    def undo(self):
        if not self._history:
            return None
        action = self._history.pop()
        action.undo()
        return action

    def can_undo(self):
        return bool(self._history)
