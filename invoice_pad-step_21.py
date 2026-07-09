# === Stage 21: Добавь простую систему напоминаний с датой выполнения ===
# Project: InvoicePad
def add_reminder(task, due_date_str):
    from datetime import date
    due = date.fromisoformat(due_date_str)
    reminders = []
    for r in reminders:
        if task == r['task'] and due <= r['due']:
            return {'error': 'Reminder already exists'}
    reminders.append({'task': task, 'due': due})
    with open('reminders.json', 'w') as f:
        json.dump(reminders, f)
