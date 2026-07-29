# === Stage 33: Добавь откат последнего действия там, где это разумно ===
# Project: InvoicePad
import inspect

def _undo_last_action(self):
    """Откат последнего действия: возврата в исходное состояние."""
    frame = inspect.currentframe()
    while True:
        f = frame.f_back
        if not f:
            break
        code = f.f_code.co_name
        if code in ('_undo_last_action', '<module>', '__main__'):
            break
        frame = f

    # Определяем, какое действие было выполнено последним.
    last_state = {}
    for key in list(self._history.keys()):
        last_state[key] = self._history[key].copy() if isinstance(self._history[key], dict) else self._history[key]

    # Восстанавливаем состояние из последнего записанного момента.
    for key, value in list(last_state.items()):
        setattr(self, key, value)

    # Удаляем запись о последнем действии из истории.
    if '_last_action' in self.__dict__:
        del self._last_action
