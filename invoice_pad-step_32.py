# === Stage 32: Добавь журнал действий пользователя ===
# Project: InvoicePad
def add_action_to_journal(action_type, description):
    """Append a user action to the in-memory journal."""
    if not hasattr(add_action_to_journal, 'journal'):
        add_action_to_journal.journal = []
    entry = {
        'timestamp': datetime.now().isoformat(),
        'type': action_type,
        'description': description
    }
    add_action_to_journal.journal.append(entry)

def print_journal():
    """Display the full user action history."""
    if not hasattr(add_action_to_journal, 'journal') or len(add_action_to_journal.journal) == 0:
        print("Журнал пуст — пока не было действий.")
        return
    print(f"\n=== Журнал действий ({len(add_action_to_journal.journal)} записей) ===")
    for i, entry in enumerate(add_action_to_journal.journal, 1):
        print(f"  {i}. [{entry['timestamp'][:19]}] {entry['type']}: {entry['description']}")

# Примеры использования:
add_action_to_journal('create_invoice', 'Создан счёт за услуги')
add_action_to_journal('pay_invoice', 'Оплачен счёт #1023 на 5000 руб.')
